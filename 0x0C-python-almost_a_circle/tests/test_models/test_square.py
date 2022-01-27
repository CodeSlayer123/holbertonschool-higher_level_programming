#!/usr/bin/python3
from models.square import Square
import unittest
"""Test for class Square"""


class SquareTest(unittest.TestCase):
    """Test for class Square"""

    @classmethod
    def setUpClass(cls):
        cls.r1 = Square(10)
        cls.r2 = Square(2, 10)
        cls.r3 = Square(10, 2, 10, 20)
        cls.r4 = Square(10, 2, 10, -10)

    @classmethod
    def tearDownClass(cls):
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4

    def test_task10(self):

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 20)
        self.assertEqual(self.r4.id, -10)

        self.assertEqual(self.r1.size, 10)
        self.assertEqual(self.r2.size, 2)
        self.assertEqual(self.r3.x, 2)
        self.assertEqual(self.r4.y, 10)

        with self.assertRaises(TypeError):
            r5 = Square()

    def test_task3(self):
        with self.assertRaises(TypeError):
            # size
            r1 = Square("hello")
            r4 = Square(None)
            r5 = Square(10.5)
            r5 = Square(True)
            r5 = Square(float('Nan'))
            r5 = Square(float('inf'))
            # x and y

            r1 = Square(10, 10, "hello")
            r2 = Square(10, "hello", 10)
            r4 = Square(10, 10, None)
            r5 = Square(10, None, 20)
            r5 = Square(10, 10, 10.5)
            r6 = Square(10, 10.5, 20)
            r5 = Square(10, 10, True)
            r6 = Square(10, True, 20)
            r5 = Square(10, 10, float('Nan'))
            r6 = Square(10, float('Nan'), 20)
            r5 = Square(10, 10, float('inf'))
            r6 = Square(10, float('inf'), 20)

        with self.assertRaises(ValueError):
            # size
            r1 = Square(-10)
            r3 = Square(0)

            # x and y
            r1 = Square(10, -10, 10)
            r2 = Square(10, 10, -10)

    def test_task4(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)
        r1.size = 10
        self.assertEqual(r1.area(), 100)

    def test_task5(self):
        r1 = Square(1)
        self.assertEqual(r1.display(), None)

    def test_task6(self):
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")

    def test_task7(self):
        r1 = Square(2, 2, 2)
        self.assertEqual(r1.display(), None)

    def test_task8(self):

        r1 = Square(10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1 = Square(10)
        r1.update(89, 2, 4)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 4)

    def test_task9(self):
        r1 = Square(10, 10, 10)

        r1.update(size=1)
        self.assertEqual(r1.size, 1)

        r1.update(size=1, x=2)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, size=2, id=89, x=3)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 89)

        r1.update(3, 4, y=5, size=2, x=0)
        self.assertEqual(r1.size, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 3)

    def test_task13(self):
        r1 = Square(10, 1, 9, 1)
        r1_dict = r1.to_dictionary()
        self.assertEqual(type(r1_dict), dict)
        self.assertEqual(r1_dict, {'id': 1, 'size': 10,
                                   'x': 1, 'y': 9})
        self.assertEqual(Square.to_json_string([]), "[]")
        self.assertEqual(Square.to_json_string(None), "[]")

    def test_task16(self):
        b1 = Square(10, 2, 8)
        b2 = Square(2)
        Square.save_to_file([b1, b2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 3, \
"size": 10, "x": 2, "y": 8}, \
{"id": 4, "size": 2, "x": 0, "y": 0}]')

    def test_task18(self):
        my_dict = {'size': 5, 'x': 8}
        rect = Square.create(**my_dict)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.size, 5)

    def test_task18(self):
        r1 = Square(10, 2, 8)
        r2 = Square(2)
        list_Squares_input = [r1, r2]

        Square.save_to_file(list_Squares_input)

        list_Squares_output = Square.load_from_file()
        self.assertEqual(str(list_Squares_output[0]),
                         '[Square] (5) 2/8 - 10')

if __name__ == '__main__':
    unittest.main()
