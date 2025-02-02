# Clean previous builds
cargo clean

# Fetch dependencies
cargo update

# Build with maturin
maturin develop --release

# Test in Python
python -c "from levenshtein_rs import similarity; print(similarity('kitten', 'sitting'))"