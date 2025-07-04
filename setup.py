#!/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="obd",
    version="0.8.0",
    description=("Serial module for handling live sensor data from a vehicle's OBD-II port over wifi suited for a Panda Adapater"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: System :: Monitoring",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: System :: Logging",
        "Intended Audience :: Developers",
    ],
    keywords="obd obdii obd-ii obd2 car serial vehicle diagnostic panda commaai",
    author="Anon Mall",
    author_email="anon.mall@gt-arc.com",
    url="https://github.com/dailab/python-OBD-wifi",
    license="GNU GPLv2",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["pyserial==3.*", "pint==0.7.*"],
)
