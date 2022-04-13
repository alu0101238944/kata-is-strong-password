
import unittest
from src.is_strong_password import is_strong_password

class IsStrongPasswordTest(unittest.TestCase):
  def test_strong_password_return_true(self):
    self.assertEqual(is_strong_password('ABab_1'), True)

if __name__ == '__main__':
  unittest.main()
