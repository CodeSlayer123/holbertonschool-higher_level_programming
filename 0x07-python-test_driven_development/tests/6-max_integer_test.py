import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_start(self):
        self.assertEqual(max_integer([5, 2, 3, 4, 1]), 5)

    def test_max_at_mid(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_one_neg(self):
        self.assertEqual(max_integer([1, 2, -3, 4, 5]), 5)

    def test_all_negs(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_one_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_no_elements(self):
        self.assertEqual(max_integer([]), None)
