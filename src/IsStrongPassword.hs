module IsStrongPassword where

import qualified Data.Char as Char (isDigit)

isStrongPassword :: String -> Bool
isStrongPassword s = length s >= 6 && any Char.isDigit s