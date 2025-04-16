# setup.py
from setuptools import setup, find_packages

setup(
    name="recommandationSystem",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'pytest',
        'faker'
    ],
)