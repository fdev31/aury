from setuptools import setup, find_packages

setup(
    name="aury",
    version="0.9",
    author="Fabien Devaux",
    author_email="fdev31@gmail.com",
    license="GPL",
    platform="all",
    description="AUR (archlinux) packages maintenance made easy via PyPi lookup",
    scripts=['aury'],
    packages=find_packages(),
)

