# Copyright (C) 2012 Linaro Limited
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

"""
lava.utils.interface
====================

Common interface class for LAVA
"""


__version__ = (1, 0, 0, "final", 0)


from abc import ABCMeta, abstractmethod, abstractproperty


class Interface(object):
    """
    Interface class.

    This trivial class simply wraps the ABCMeta metaclass so you don't have to
    worry about it much.
    """

    __metaclass__ = ABCMeta
