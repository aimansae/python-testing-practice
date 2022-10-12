import unittest
from evens import even_numbers

# always start the class with test and give unittest.TestCase arg
# def test_function_return_True(self):
# self.assertTrue(even_numbers([]))


class TestEvens(unittest.TestCase):
    # always start the function with test give arg self
    def test_throws_error_if_value_passed_is_not_list(self):
        self.assertRaises(TypeError, even_numbers, 4)

    def test_values_in_list(self):
        self.assertEqual(even_numbers([]), False)
        self.assertEqual(even_numbers([2, 4]), True)
        self.assertEqual(even_numbers([2]), False)
        self.assertEqual(even_numbers([1, 3, 5]), False)


if __name__ == '__main__':
    unittest.main()
