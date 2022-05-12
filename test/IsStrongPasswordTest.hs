module Main where

import IsStrongPassword
import Test.Hspec

{-
  Requirements:
  * At least 6 characters
  * At least one number
  * At least one upper case letter
  * At least one lower case letter
  * At least one underscore
-}

main :: IO ()
main = hspec isStrongPasswordTests

isStrongPasswordTests :: Spec
isStrongPasswordTests = describe "IsStrongPassword behaviour" $ do
  it "A strong password should be accepted" $ do
    isStrongPassword "Ab_2ef" `shouldBe` True

  it "A password with less than 6 characters shouldn't be accepted" $ do
    isStrongPassword "Ab_2e" `shouldBe` False

  it "A password without a number shouldn't be accepted" $ do
    isStrongPassword "Ab_def" `shouldBe` False

  it "A password without an upper case letter shouldn't be accepted" $ do
    isStrongPassword "ab_2ef" `shouldBe` False
