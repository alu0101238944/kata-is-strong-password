module IsStrongPassword where

import qualified Data.Char as Char (isDigit, isLower, isUpper)

isStrongPassword :: String -> Bool
isStrongPassword s =
  length s >= 6
    && any Char.isDigit s
    && any Char.isUpper s
    && any Char.isLower s