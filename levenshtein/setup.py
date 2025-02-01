from setuptools import setup, Extension

module = Extension(
    'clevenshtein',
    sources=['levenshtein.c'],
    extra_compile_args=['-O3', '-march=native'],
)

setup(
    name='clevenshtein',
    version='1.0',
    description='High-performance Levenshtein similarity calculator',
    ext_modules=[module],
)
