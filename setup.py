from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='connect_mongodb',
    version='0.0.1',
    description='Connect mongoDb with python',
    author='Karan Jani',
    url='https://github.com/KaranJani/PyPi-connect_mongodb',
    long_description='Refer Readme',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['mongodb', 'python', 'connect mongodb with python', 'connect to mongodb'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['connect_mongodb'],
    install_requires=['pymongo']
    )
