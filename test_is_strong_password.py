
import unittest
from src.is_strong_password import IsStrongPassword

class IsStrongPasswordTest(unittest.TestCase):
  def setUp(self):
    self.is_strong_password = IsStrongPassword()

  def test_strong_password_is_valid(self):
    self.assertEqual(self.is_strong_password.check('ABab_1'), True)

  def test_password_must_have_at_least_six_characters(self):
    self.assertEqual(self.is_strong_password.check('Aab1_'), False)

  def test_password_must_have_at_least_one_uppercase_letter(self):
    self.assertEqual(self.is_strong_password.check('abcd_1'), False)

  def test_password_must_have_at_least_one_lowercase_letter(self):
    self.assertEqual(self.is_strong_password.check('ABCD_1'), False)

  def test_password_must_have_at_least_one_digit(self):
    self.assertEqual(self.is_strong_password.check('ABabc_'), False)

  def test_password_must_have_at_least_one_underscore(self):
    self.assertEqual(self.is_strong_password.check('ABabc1'), False)


if __name__ == '__main__':
  unittest.main()
