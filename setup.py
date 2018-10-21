from setuptools import setup, find_packages

setup(
    name="pocket-cli",
    version="0.1",
    author="Juan Latorre",
    author_email="juanlatorre@protonmail.com",
    url="https://github.com/juanlatorre/pocket-cli",

    license="LICENSE",
    description="Pocket Cli app through command line",
    long_description=open("README.md").read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires = [
        "Click",
        "pocket-api",
    ],

    entry_points={
        "console_scripts": [
            "pocket-cli=pocketcli.app:main"
        ]
    }
)
