import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pystab-AurigaDev",
    version= "0.0.1",
    author="pain2141@gmail.com",
    name="pain2141",
    description="A python port of Jakstab by Kinder",
    long_description=long_description,
    long_descprition_content_type="text/markdown",
    url="https://gitlab.com/AurigaDev/pystab",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent"
    ],
)
