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
lava.utils.interface.tests
==========================

Unit tests for the interface class
"""

import unittest2

from lava.utils.interface import Interface, abstractmethod, abstractproperty


class IAnimal(Interface):
    """
    Animal interface, you can pat and call your pupils
    """

    @abstractmethod
    def pat(self):
        """
        Pat this animal, returns a string of what the reaction is
        """

    @abstractproperty
    def name(self):
        """
        Name of this animal
        """


class Dog(IAnimal):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def pat(self):
        return "The dog wiggles its tail"


class InterfaceTests(unittest2.TestCase):

    def test_raises_exceptions_for_missing_methods(self):
        self.assertRaises(TypeError, IAnimal)

    def test_full_subclasses_work(self):
        bit = Dog("bit")
        self.assertEqual(bit.name, "bit")
        self.assertEqual(bit.pat(), "The dog wiggles its tail")
