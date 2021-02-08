import unittest
import cube

class TestCase(unittest.TestCase):
    def test_negative(self):
        result = cube.volumeCube(-1, 5, -1)
        self.assertEqual(result, 5)
        result = cube.volumeCube(-1, 5, 2)
        self.assertEqual(result, -10)
        result = cube.volumeCube(-5, -5, -5)
        self.assertEqual(result, -125)
    def test_floats(self):
        result = cube.volumeCube(2.5, 5, 1.5)
        self.assertEqual(result, 18.75)
        result = cube.volumeCube(12, .5, 1)
        self.assertEqual(result, 6)
    def test_type(self):
        result = cube.volumeCube("hi", 'a', 7)
        self.assertEqual(result, None)
if __name__ == '__main__':
    unittest.main(verbosity=2)
