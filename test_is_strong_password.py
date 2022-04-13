
import unittest
from src.is_strong_password import is_strong_password

class IsStrongPasswordTest(unittest.TestCase):
  def test_strong_password_return_true(self):
    self.assertEqual(is_strong_password('ABab_1'), True)

  def test_password_must_have_at_least_six_characters(self):
    self.assertEqual(is_strong_password(''), False)
    self.assertEqual(is_strong_password('A'), False)
    self.assertEqual(is_strong_password('Aa'), False)
    self.assertEqual(is_strong_password('Aa1'), False)
    self.assertEqual(is_strong_password('Aa1_'), False)
    self.assertEqual(is_strong_password('Aa1_b'), False)

if __name__ == '__main__':
  unittest.main()
