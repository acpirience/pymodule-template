import io
import os
import re

from collections import OrderedDict
from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


setup(
    name="PROJECT",
    version="0.0.1",
    url="https://github.com/acpirience/PROJECT",
    project_urls=OrderedDict(
        (
            ("Documentation", "https://PROJECT.readthedocs.io"),
            ("Code", "https://github.com/acpirience/PROJECT"),
        )
    ),
    author="Acpirience",
    author_email="acpirience@gmail.com",
    description="DESCRIPTION",
    long_description=read("README.rst"),
    platforms="any",
    packages=find_packages(exclude=("tests",)),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
