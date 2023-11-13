import unittest
from math_quiz import generate_num1, generate_operation, operation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_num1(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if random operator generated is one of the specified operators
        for _ in range(100):
            rand_operator = generate_operation()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 3, '-', '5 - 3', 2),
                (1, 6, '*', '1 * 6', 6),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = operation(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
