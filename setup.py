import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="Brute"
    version="0.0.1",
    author="Lee Enck",
    author_email="laenck192@stevenscollege.edu",
    url="https://github.com/LeeEnck/Brute",
    description="This is a text adventure game.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
