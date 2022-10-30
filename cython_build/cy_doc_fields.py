import pathlib

from setuptools import setup
from Cython.Build import cythonize
import os
file=os.path.join(pathlib.Path(__file__).parent.parent.__str__(),"code",f"cy_doc_fields.py")
print(file)
setup(
    name='cy_docs',
    ext_modules=cythonize(file),
    zip_safe=True,
)
"""
python cython_build/cy_doc_fields.py build_ext --inplace
"""