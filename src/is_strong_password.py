
class IsStrongPassword():
  def __thereIsUpperCaseLetter(self, password):
    return any(map(lambda char: char.isupper(), password))

  def __thereIsLowerCaseLetter(self, password):
    return any(map(lambda char: char.islower(), password))

  def __thereIsDigit(self, password):
    return any(map(lambda char: char.isdigit(), password))

  def __thereIsUnderscore(self, password):
    return any(map(lambda char: char == '_', password))

  def apply(self, password: str):
    return (
      len(password) >= 6 and
      self.__thereIsUpperCaseLetter(password) and
      self.__thereIsLowerCaseLetter(password) and 
      self.__thereIsDigit(password) and 
      self.__thereIsUnderscore(password)
    )
