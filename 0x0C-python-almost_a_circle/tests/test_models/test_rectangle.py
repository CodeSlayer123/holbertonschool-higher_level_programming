#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
"""Test for class rectangle"""


class RectangleTest(unittest.TestCase):
    """Test for class rectangle"""

    @classmethod
    def setUpClass(cls):
        """Setting up class"""
        cls.r1 = Rectangle(10, 2)
        cls.r2 = Rectangle(2, 10)
        cls.r3 = Rectangle(10, 2, 0, 0, 12)
        cls.r4 = Rectangle(10, 2, 0, 0, -12)

    @classmethod
    def tearDownClass(cls):
        """Tearing down class"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4

    def test_task2(self):

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.id, -12)

    def test_task3(self):
        with self.assertRaises(TypeError):
            # width and height
            r1 = Rectangle(10, "hello")
            r2 = Rectangle("hello", 10)
            r4 = Rectangle(10, None)
            r5 = Rectangle(None, 20)
            r5 = Rectangle(10, 10.5)
            r6 = Rectangle(10.5, 20)
            r5 = Rectangle(10, True)
            r6 = Rectangle(True, 20)
            r5 = Rectangle(10, float('Nan'))
            r6 = Rectangle(float('Nan'), 20)
            r5 = Rectangle(10, float('inf'))
            r6 = Rectangle(float('inf'), 20)
            # x and y

            r1 = Rectangle(10, 10, 10, "hello")
            r2 = Rectangle(10, 10, "hello", 10)
            r4 = Rectangle(10, 10, 10, None)
            r5 = Rectangle(10, 10, None, 20)
            r5 = Rectangle(10, 10, 10, 10.5)
            r6 = Rectangle(10, 10, 10.5, 20)
            r5 = Rectangle(10, 10, 10, True)
            r6 = Rectangle(10, 10, True, 20)
            r5 = Rectangle(10, 10, 10, float('Nan'))
            r6 = Rectangle(10, 10, float('Nan'), 20)
            r5 = Rectangle(10, 10, 10, float('inf'))
            r6 = Rectangle(10, 10, float('inf'), 20)

        with self.assertRaises(ValueError):
            # width and height
            r1 = Rectangle(10, -10)
            r2 = Rectangle(-10, 10)
            r3 = Rectangle(10, 0)
            r4 = Rectangle(0, 10)

            # x and y
            r1 = Rectangle(10, 10, 10, -10)
            r2 = Rectangle(10, 10, -10, 10)

    def test_task4(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 10
        self.assertEqual(r1.area(), 20)

    def test_task5(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.display(), None)

    def test_task6(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_task7(self):
        r1 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r1.display(), None)

    def test_task8(self):

        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        r1 = Rectangle(10, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

    def test_task9(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, id=89, x=3)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 89)

        r1.update(3, 4, y=5, width=2, x=0)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 3)

    def test_task13(self):
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(r1_dict, {'id': 1, 'width': 10, 'height': 2,
                                   'x': 1, 'y': 9})
        self.assertEqual(Rectangle.to_json_string([]), "[]")
        self.assertEqual(Rectangle.to_json_string(None), "[]")

    def test_task16(self):
        b1 = Rectangle(10, 7, 2, 8)
        b2 = Rectangle(2, 4)
        Rectangle.save_to_file([b1, b2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 3, \
"width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 4, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_task18(self):
        my_dict = {'height': 5, 'width': 3, 'x': 8}
        rect = Rectangle.create(**my_dict)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 5)

    def test_task18(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]),
                         '[Rectangle] (5) 2/8 - 10/7')

if __name__ == '__main__':
    unittest.main()
