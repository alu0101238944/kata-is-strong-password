
class IsStrongPassword():
  def __thereIsUpperCaseLetter(self, password):
    for char in password:
      if char.isupper():
        return True
    return False

  def apply(self, password: str):
    return len(password) >= 6 and self.__thereIsUpperCaseLetter(password)
