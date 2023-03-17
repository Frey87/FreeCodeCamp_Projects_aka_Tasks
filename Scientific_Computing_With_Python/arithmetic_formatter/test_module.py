import unittest
from arithmetic_arranger import arithmetic_arranger
from contextlib import redirect_stdout
from io import StringIO
  # test
class UnitTests(unittest.TestCase):
  def test_too_many_problems(self):
    with redirect_stdout(StringIO()) as sout:
      arithmetic_arranger(["412 + 856", "911 - 34", "344 + 4345", "234 + 78", "203 + 55", "29 + 46"])
    retval = sout.getvalue().rstrip('\n')
    self.assertEqual(retval, "Error: Too many problems.")

  def test_too_many_digits(self):
    with redirect_stdout(StringIO()) as sout:
      arithmetic_arranger(["412 + 85644", "911 - 34", "344 + 4345", "234 + 78"])        
    retval = sout.getvalue().rstrip('\n')
    self.assertEqual(retval, "Error: Numbers cannot be more than four digits.")
  
  def test_divide_operator(self):
    with redirect_stdout(StringIO()) as sout:
      arithmetic_arranger(["412 / 854", "911 - 34", "344 + 4345", "234 + 78"])        
    retval = sout.getvalue().rstrip('\n')
    self.assertEqual(retval, "Error: Operator must be '+' or '-'.")

  def test_multiply_operator(self):
    with redirect_stdout(StringIO()) as sout:
      arithmetic_arranger(["412 * 854", "911 - 34", "344 + 4345", "234 + 78"])        
    retval = sout.getvalue().rstrip('\n')
    self.assertEqual(retval, "Error: Operator must be '+' or '-'.")
    
  
if __name__ == '__main__':
    unittest.main()
