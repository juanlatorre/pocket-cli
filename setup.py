from setuptools import setup, find_packages

setup(
    name="pocketcli",
    version="0.2",
    author="Juan Latorre",
    author_email="juanlatorre@protonmail.com",
    url="https://github.com/juanlatorre/pocketcli",

    license="LICENSE",
    description="Pocket Cli app through command line",
    long_description=open("README.md").read(),

    packages=find_packages(),
    include_package_data=True,

    install_requires = [
        "Click",
        "pocket-api",
        "requests"
    ],

    entry_points={
        "console_scripts": [
            "pocketcli=pocketcli.app:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
