from setuptools import setup


with open("README.md") as f:
    long_description = f.read()


setup(
    name="opengrapher",
    packages=["opengrapher"],
    version="0.2.2",
    description="Utility for parsing the OpenGraph tags",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="opengraph",
    author="Maxim Semenov",
    author_email="0rang3max@gmail.com",
    url="https://github.com/0rang3max/opengrapher",
    download_url="https://github.com/0rang3max/opengrapher/archive/v0.2.tar.gz",
    license="MIT",
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=["beautifulsoup4", "requests"],
    entry_points="""
      # -*- Entry points: -*-
    """,
)
