from setuptools import setup, find_packages

setup(
    name='ai_seed',
    version='0.1.0',
    author='Hammad Usmani',
    author_email='hammadus@gmail.com',
    description='A Python package for generating random numbers using TPM 2.0 for TRNG with reproducibility for data science.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'tpm2-pytss',
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)