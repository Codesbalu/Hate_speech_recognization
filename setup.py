from setuptools import find_packages, setup

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME="Hate_speech_recognization"
AUTHOR_USER_NAME="Codesbalu"
SRC_REPO="hate_speech"
LIST_OF_REQUIREMENTS=[]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Codesbalu",
    description="A small local packages for NLP based Hate speech recognization",
    long_description=long_description,
    url="https://github.com/Codesbalu/Hate_speech_recognization.git",
    auhtor_email="balajibalusbvb@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)