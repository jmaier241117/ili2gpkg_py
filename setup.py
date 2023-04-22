import os
from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    author="Jamie Maier",
    author_email='jamiemaier98@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
    ],
    description="Python package for ili2gpkg.",
    install_requires=['importlib-resources'] ,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='ili2gpkg,interlis',
    name='ili2gpkg',
    url='https://github.com/jmaier241117/ili2gpkg_py',
    packages=find_packages(include=['ili2gpkg', 'ili2gpkg.*']),
    package_data={'ili2gpkg.lib_ext':['*.h', '*.lib', '*.dll', '*.so', '*.dylib']},
    version='0.0.2',
)