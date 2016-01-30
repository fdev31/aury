from setuptools import setup, find_packages

setup(
    name="aury",
    version="1.1.2",
    author="Fabien Devaux",
    author_email="fdev31@gmail.com",
    license="MIT",
    platform="all",
    description="AUR (archlinux) packages maintenance made easy via PyPi lookup",
    long_description=open('README.md').read(),
    scripts=['aury'],
    packages=find_packages(),
    url='https://github.com/fdev31/aury',
    zip_safe=True,
    keywords=['packaging', 'archlinux', 'automate', 'aur', 'pacman'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Archiving :: Packaging',
    ]
)

