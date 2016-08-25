import unittest

from test_util import ScanPointGeneratorTest
from scanpointgenerator.mutator import Mutator

from pkg_resources import require
require("mock")
from mock import MagicMock


class MutatorTest(unittest.TestCase):

    def test_mutate_raises(self):
        m = Mutator()
        with self.assertRaises(NotImplementedError):
            m.mutate(MagicMock())

    def test_register_subclass(self):

        @Mutator.register_subclass("TestMutator")
        class TestMutator(object):
            pass

        self.assertEqual(TestMutator, Mutator._mutator_lookup["TestMutator"])
        self.assertEqual("TestMutator", TestMutator.typeid)


class SerialisationTest(unittest.TestCase):

    def setUp(self):
        self.m = Mutator()

    def test_to_dict_raises(self):
        with self.assertRaises(NotImplementedError):
            self.m.to_dict()

    def test_from_dict(self):
        m = MagicMock()
        self.m._mutator_lookup['TestMutator'] = m

        gen_dict = dict(type="TestMutator")
        self.m.from_dict(gen_dict)

        m.from_dict.assert_called_once_with(gen_dict)

if __name__ == "__main__":
    unittest.main()
