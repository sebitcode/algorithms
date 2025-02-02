# Clean previous builds
rm -rf build dist *.so *.cpython-*

# Compile fresh
python setup.py build_ext --inplace

# Verify
python -c "import clevenshtein; print(clevenshtein.similarity('test', 'test'))"  # Should print 100.0