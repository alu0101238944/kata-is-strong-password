
class IsStrongPassword():
  def __thereIsUpperCaseLetter(self, password):
    return any(map(lambda char: char.isupper(), password))

  def apply(self, password: str):
    return len(password) >= 6 and self.__thereIsUpperCaseLetter(password)
