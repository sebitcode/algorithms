use pyo3::prelude::*;
use pyo3::types::PyModule;
use pyo3::Bound;

#[pyfunction]
fn similarity(word1: &str, word2: &str) -> f64 {
    // Early exit for identical words
    if word1 == word2 {
        return 100.0;
    }

    // Handle empty cases
    if word1.is_empty() || word2.is_empty() {
        return 0.0;
    }

    // Swap to use the shorter word for the inner loop
    let (word1, word2) = if word1.len() < word2.len() {
        (word2, word1)
    } else {
        (word1, word2)
    };

    let len1 = word1.len();
    let len2 = word2.len();

    // Initialize DP row with 0..len2
    let mut row: Vec<usize> = (0..=len2).collect();

    for i in 1..=len1 {
        let mut prev = row[0];
        let char1 = word1.chars().nth(i - 1).unwrap();
        row[0] = i;

        for j in 1..=len2 {
            let char2 = word2.chars().nth(j - 1).unwrap();
            let sub_cost = if char1 == char2 { 0 } else { 1 };

            let current = row[j];
            row[j] = (current + 1)        // Deletion
                .min(row[j - 1] + 1)      // Insertion
                .min(prev + sub_cost);    // Substitution

            prev = current;
        }
    }

    // Calculate similarity percentage
    let max_len = len1.max(len2) as f64;
    let similarity = (1.0 - (row[len2] as f64) / max_len) * 100.0;
    similarity
}

#[pymodule]
fn levenshtein_rs(_py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(similarity, m)?)?;
    Ok(())
}