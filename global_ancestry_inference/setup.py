from setuptools import setup, find_packages

setup(
    name="global_ancestry_inference",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scipy>=1.7.0",
    ],
    entry_points={
        "console_scripts": [
            "global_ancestry_inference=src.main:main",
        ],
    },
)