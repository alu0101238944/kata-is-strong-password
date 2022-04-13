
import unittest
from src.is_strong_password import IsStrongPassword

class IsStrongPasswordTest(unittest.TestCase):
  def setUp(self):
    self.is_strong_password = IsStrongPassword()

  def test_strong_password_return_true(self):
    self.assertEqual(self.is_strong_password.apply('ABab_1'), True)

  def test_password_must_have_at_least_six_characters(self):
    self.assertEqual(self.is_strong_password.apply('Aab1_'), False)

  def test_password_must_have_at_least_one_uppercase_letter(self):
    self.assertEqual(self.is_strong_password.apply('abcd_1'), False)

  def test_password_must_have_at_least_one_lowercase_letter(self):
    self.assertEqual(self.is_strong_password.apply('ABCD_1'), False)

  def test_password_must_have_at_least_one_digit(self):
    self.assertEqual(self.is_strong_password.apply('ABabc_'), False)


if __name__ == '__main__':
  unittest.main()
