import unittest
import names

class TestCase(unittest.TestCase):
    def test_type(self):
        result = names.generateName("Joe", 2312)
        self.assertEqual(result, "Not a valid type.")
        result = names.generateName(123.5, 13)
        self.assertEqual(result, "Not a valid type.")
    def test_correct(self):
        result = names.generateName("Joe", "Biden")
        self.assertEqual(result, "Joe Biden")
        result = names.generateName("Matt", "Watson")
        self.assertEqual(result, "Matt Watson")
        result = names.generateName("Levi", "Ackerman")
        self.assertEqual(result, "Levi Ackerman")
    def test_spaces(self):
        result = names.generateName("This123", "Isn0tvalid")
        self.assertEqual(result, "Name can't contain numbers.")
if __name__ == '__main__':
    unittest.main(verbosity=2)