/* levenshtein.c */
#include <Python.h>
#include <stdlib.h>

#define MIN3(a, b, c) ((a) < (b) ? ((a) < (c) ? (a) : (c)) : ((b) < (c) ? (b) : (c)))

static PyObject* levenshtein_similarity(PyObject* self, PyObject* args) {
    PyObject *w1, *w2;
    Py_ssize_t len1, len2;
    
    if (!PyArg_ParseTuple(args, "UU", &w1, &w2)) return NULL;
    
    // Content-based equality check
    if (PyUnicode_Compare(w1, w2) == 0) {
        return PyFloat_FromDouble(100.0);
    }
    
    len1 = PyUnicode_GET_LENGTH(w1);
    len2 = PyUnicode_GET_LENGTH(w2);
    
    // Handle empty strings after equality check
    if (!len1 || !len2) {
        return PyFloat_FromDouble(0.0);
    }
    
    // Swap to use shorter string for inner loop
    if (len2 > len1) {
        PyObject* tmp = w1;
        w1 = w2;
        w2 = tmp;
        Py_ssize_t t = len1;
        len1 = len2;
        len2 = t;
    }
    
    const Py_ssize_t max_len = len1;  // After swap, len1 >= len2
    
    // Convert to code point arrays
    Py_UCS4 *s1 = (Py_UCS4*)malloc(len1 * sizeof(Py_UCS4));
    Py_UCS4 *s2 = (Py_UCS4*)malloc(len2 * sizeof(Py_UCS4));
    if (!s1 || !s2) {
        free(s1);
        free(s2);
        PyErr_NoMemory();
        return NULL;
    }
    
    for (Py_ssize_t i = 0; i < len1; ++i) s1[i] = PyUnicode_ReadChar(w1, i);
    for (Py_ssize_t i = 0; i < len2; ++i) s2[i] = PyUnicode_ReadChar(w2, i);
    
    // Initialize DP array
    Py_ssize_t *row = (Py_ssize_t*)malloc((len2 + 1) * sizeof(Py_ssize_t));
    if (!row) {
        free(s1);
        free(s2);
        PyErr_NoMemory();
        return NULL;
    }
    
    for (Py_ssize_t j = 0; j <= len2; ++j) row[j] = j;
    
    // Main calculation loop
    for (Py_ssize_t i = 1; i <= len1; ++i) {
        Py_ssize_t prev = row[0];
        row[0] = i;
        const Py_UCS4 c1 = s1[i-1];
        
        for (Py_ssize_t j = 1; j <= len2; ++j) {
            const Py_ssize_t current = row[j];
            const Py_ssize_t sub_cost = (c1 != s2[j-1]);
            
            row[j] = MIN3(
                current + 1,    // Deletion
                row[j-1] + 1,   // Insertion
                prev + sub_cost // Substitution
            );
            prev = current;
        }
    }
    
    const double similarity = (1.0 - (double)row[len2]/max_len) * 100.0;
    
    free(s1);
    free(s2);
    free(row);
    
    return PyFloat_FromDouble(similarity);
}

static PyMethodDef methods[] = {
    {"similarity", levenshtein_similarity, METH_VARARGS, "Calculate string similarity"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "clevenshtein",
    "Fast Levenshtein similarity in C",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_clevenshtein(void) {
    return PyModule_Create(&module);
}