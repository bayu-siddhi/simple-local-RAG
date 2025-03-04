from os import path
from codecs import open
from setuptools import setup
from setuptools import find_packages

# Root directory
root = path.abspath(path.dirname(__file__))


def read_file(file: str):
    """Read file in this (root) directory"""
    with open(path.join(root, file), encoding='utf-8') as f:
        return f.read()


def read_version():
    """Read __version__.py"""
    data = dict()
    # project = NAME.lower().replace("-", "_").replace(" ", "_")
    project = NAME.replace("-", "_").replace(" ", "_")
    with open(path.join(root, project, '__version__.py')) as f:
        exec(f.read(), data)
        return data['__version__']


# Package meta-data
NAME = 'simple_RAG'
VERSION = read_version()
SHORT_DESC = 'library to try using RAG from PDF files. Runs using the LLM model and embedding model from HuggingFace'
LONG_DESC = read_file('README.md')
URL = 'https://github.com/bayu-siddhi/simple-RAG'
AUTHOR = 'test'
EMAIL = 'test@test.test'
REQUIRES_PYTHON = '>=3.9.0'
REQUIRED = read_file("requirements.txt").splitlines()

# This call to setup() does all the work
setup(
    name=NAME,
    version=VERSION,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=['tests']),
    install_requires=REQUIRED
)
