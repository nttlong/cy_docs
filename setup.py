from setuptools import setup
from Cython.Build import cythonize

setup(
    name='cy_docs',
    ext_modules=cythonize("cy_doc_fields.py"),
    zip_safe=True,
)