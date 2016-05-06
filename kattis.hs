module Kattis where

import Data.Char (digitToInt)

digitSum :: Int -> Int
digitSum n = sum $ map digitToInt (show n)