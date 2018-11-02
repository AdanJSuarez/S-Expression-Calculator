# S-expressions calculator
# Adan J. Suarez

import unittest
from model.compute_expression import Compute_Expression as ce

class TestComputeExpression(unittest.TestCase):

    def setUp(self):
        self.expr1 = "123"
        self.expr2 = "00"
        self.expr3 = "(add 1 1)"
        self.expr4 = "(multiply (add 1 2) 3)"
        self.expr5 = "(multiply 2 3)"
        self.expr11 = "(add 33 (multiply 2 4))"
        self.expr13 = "9)"
        self.expr15 = "(multiply (add (add 1 2) 2) (add (multiply 2 3) 57))"
        self.expr17 = "(multiply (multiply 5 (add 1 1)) (add (add 3 4) (add 4 8)))"
        self.expr6 = ce(self.expr1)
        self.expr7 = ce(self.expr2)
        self.expr8 = ce(self.expr3)
        self.expr9 = ce(self.expr4)
        self.expr10 = ce(self.expr5)
        self.expr12 = ce(self.expr11)
        self.expr14 = ce(self.expr13)
        self.expr16 = ce(self.expr15)
        self.expr18 = ce(self.expr17)

    def test_expr_integer(self):
        actual = self.expr6.get_value()
        expected = 123
        self.assertEqual(actual, expected, "test1")

        actual = self.expr7.get_value()
        expected = 0
        self.assertEqual(actual, expected, "test2")

        actual = self.expr14.calc_expression(self.expr13)
        expected = 9
        self.assertEqual(actual, expected, "test int ending in )")

    def test_calc_complex_expr(self):
        actual = self.expr9.calc_complex_expression(self.expr4)
        expected = 9
        self.assertEqual(actual, expected, "test parse_complex_expression1")

        actual = self.expr12.calc_complex_expression(self.expr11)
        expected = 41
        self.assertEqual(actual, expected, "test parse_complex_expression2")

    def test_extract_function(self):
        actual = self.expr8.extract_function(self.expr3)
        expected = "add"
        self.assertEqual(actual, expected, "extract function 1")

        actual = self.expr10.extract_function(self.expr5)
        expected = "multiply"
        self.assertEqual(actual, expected, "extract function 2")

    def test_extract_expression(self):
        self.expr9.set_pointer(10)
        actual = self.expr9.extract_expression(self.expr4)
        expected = "(add 1 2)"
        self.assertEqual(actual, expected, "extract expression1") 

        self.expr9.set_pointer(20)
        actual = self.expr9.extract_expression(self.expr4)
        expected = "3)"
        self.assertEqual(actual, expected, "extract expression2")

    def test_calc_expression(self):
        actual = self.expr9.get_value()
        expected = 9
        self.assertEqual(actual, expected, "testFinal1")

        actual = self.expr12.get_value()
        expected = 41
        self.assertEqual(actual, expected, "testFinal2")

        actual = self.expr16.get_value()
        expected = 315
        self.assertEqual(actual, expected, "testFinal3")

        actual = self.expr18.get_value()
        expected = 190
        self.assertEqual(actual, expected, "testFinal4")

if __name__ == '__main__':
    unittest.main()
