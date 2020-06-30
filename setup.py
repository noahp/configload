# -*- coding: utf-8 -*-

"""
Package setup.

Set me up with `python setup.py bdist_wheel --universal`
"""
import io

from setuptools import setup

# Get long description from readme
with io.open("README.md", "rt", encoding="utf8") as readmefile:
    README = readmefile.read()

setup(
    name="py-configfile",
    version="0.0.1",
    description="Map various config file formats to python dataclass",
    author="Noah Pendleton",
    author_email="2538614+noahp@users.noreply.github.com",
    url="https://github.com/noahp/py-configfile",
    project_urls={
        "Code": "https://github.com/noahp/py-configfile",
        "Issue tracker": "https://github.com/noahp/py-configfile/issues",
    },
    long_description=README,
    long_description_content_type="text/markdown",
    extras_require = {
        'yaml':  ["pyyaml"],
        'toml':  ["tomlkit==0.6.*"],
    },
    # using markdown as pypi description:
    # https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi
    setup_requires=["setuptools>=38.6.0", "wheel>=0.31.0", "twine>=1.11.0"],
    packages=["py_configfile"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
