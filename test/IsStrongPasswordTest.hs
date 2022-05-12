module Main where

import IsStrongPassword
import Test.Hspec

{-
 Se trata de programar una función booleana que indica si una contraseña dada cumple con
unos requisitos de fortaleza. Para que la función produzca un resultado verdadero, la contraseña
debe de:
• Tener una longitud de al menos séis caracteres
• Contener algún número
• Contener alguna letra mayúscula
• Contener alguna letra minúscula
• Contener algún guión bajo (underscore)
Son estas contraseñas de las que nunca me acuerdo. La firma de la función sería algo como esto:
1 public bool IsStrongPassword(string password); 
-}

main :: IO ()
main = hspec isStrongPasswordTests

isStrongPasswordTests :: Spec
isStrongPasswordTests = describe "IsStrongPassword behaviour" $ do
  it "Simple test" $ do
    1 + 1 `shouldBe` 2

  