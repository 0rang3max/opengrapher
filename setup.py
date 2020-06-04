from setuptools import setup, find_packages
import sys, os

version = "0.1"

setup(
    name="opengrapher",
    version=version,
    description="A module to parse the OpenGraph Protocol",
    long_description=open("README.rst").read() + "\n",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="opengraph",
    author="Maxim Semenov",
    author_email="0rang3max@gmail.com",
    url="https://github.com/0rang3max/opengrapher",
    license="MIT",
    packages=find_packages(exclude=["ez_setup", "tests"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.4",
    install_requires=["beautifulsoup4", "requests"],
    entry_points="""
      # -*- Entry points: -*-
    """,
)
