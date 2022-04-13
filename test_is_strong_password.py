
import unittest
from src.is_strong_password import is_strong_password

class IsStrongPasswordTest(unittest.TestCase):
  def test_strong_password_return_true(self):
    self.assertEqual(is_strong_password('ABab_1'), True)

  def test_password_must_have_at_least_six_characters(self):
    self.assertEqual(is_strong_password('Aab1_'), False)

  def test_password_must_have_at_least_one_uppercase_letter(self):
    self.assertEqual(is_strong_password('abcd_1'), False)


if __name__ == '__main__':
  unittest.main()
