#!/usr/bin/python3
from models.base import Base
import unittest
import pep8
"""Test for class base"""


class BaseTest(unittest.TestCase):
    """Test for class base"""

    def test_task1(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(5)
        b5 = Base(-5)
        b6 = Base(42)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 5)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 42)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

        with self.assertRaises(TypeError):
            b9 = Base(1, 1, 1)

    def test_task15(self):
        my_dict = {'width': 10, 'height': 7, 'x': 2, 'y': 8, 'id': 1}
        json_dict = Base.to_json_string([my_dict])

        self.assertEqual(type(my_dict), dict)
        self.assertEqual(type(json_dict), str)
        self.assertEqual(my_dict, {'x': 2, 'width': 10, 'id': 1,
                                   'height': 7, 'y': 8})
        self.assertEqual(json_dict, '[{"width": 10, "height": 7, \
"x": 2, "y": 8, "id": 1}]')
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_task17(self):
        json_str = '[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 1}]'
        output = Base.from_json_string(json_str)
        self.assertEqual(output, [{"width": 10, "height": 7,
                                   "x": 2, "y": 8, "id": 1}])

    def test_pep8_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_test_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):

        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):

        self.assertTrue(len(Base.__doc__) >= 1)


if __name__ == '__main__':
    unittest.main()
