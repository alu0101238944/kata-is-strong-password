module IsStrongPassword where

isStrongPassword :: String -> Bool
isStrongPassword s = length s >= 6 