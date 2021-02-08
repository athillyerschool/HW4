import unittest
import listAverage

class TestCase(unittest.TestCase):
    def test_empty(self):
        stuff = []
        result = listAverage.average(stuff)
        self.assertEqual(result, None)
    def test_integer(self):
        stuff = [2, 2, 2]
        result = listAverage.average(stuff)
        self.assertEqual(result, 2)
        stuff = [2, 4, 6]
        result = listAverage.average(stuff)
        self.assertEqual(result, 4)
        result = listAverage.average(stuff)
        stuff = [1, 2, 3]
        result = listAverage.average(stuff)
        self.assertEqual(result, 2)
        stuff = [1, 4, 5, 7, 4, 7, 8, 4]
        result = listAverage.average(stuff)
        self.assertEqual(result, 5)
    def test_floats(self):
        stuff = [2.5, 2.5, 2.5]
        result = listAverage.average(stuff)
        self.assertEqual(result, 2.5)
        stuff = [1, 0, 0]
        result = listAverage.average(stuff)
        self.assertAlmostEqual(result, 0.33333333)
        stuff = [7, 3, 55]
        result = listAverage.average(stuff)
        self.assertAlmostEqual(result, 21.66666666)
        stuff = [1, 5, 7, 4, 6, 4, 8, 9]
        result = listAverage.average(stuff)
        self.assertEqual(result, 5.5)
if __name__ == '__main__':
    unittest.main(verbosity=2)
