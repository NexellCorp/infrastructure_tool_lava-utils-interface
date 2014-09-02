#!/usr/bin/env python
#
# Copyright (C) 2010 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of LAVA Utils Interface.
#
# LAVA Utils Interface is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# LAVA Utils Interface is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with LAVA Utils Interface.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages


setup(
    name='lava-utils-interface',
    version=":versiontools:lava.utils.interface:__version__",
    author="Zygmunt Krynicki",
    author_email="zygmunt.krynicki@linaro.org",
    namespace_packages=['lava', 'lava.utils'],
    packages=find_packages(),
    test_suite="unittest2.collector",
    license="LGPL",
    description="Common interface class for LAVA",
    long_description="""
    A quite trivial package with generic abstract intraface class for LAVA.  It
    may look like an overkill but I'm tired of copy-pasting this code around.
    """,
    url='https://launchpad.net/lava-utils-interface',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        ("License :: OSI Approved :: GNU Library or Lesser General Public"
         " License (LGPL)"),
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    setup_requires=['versiontools >= 1.8'],
    tests_require=['unittest2'],
    zip_safe=True,
    include_package_data=True)
