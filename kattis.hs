module Kattis where

import Data.Char (digitToInt)

digitSum :: Int -> Int
digitSum n = sum $ map digitToInt (show n)

matrixify :: Int -> [a] -> [[a]]
matrixify _ [] = []
matrixify n ls = take n ls : matrixify n (drop n ls)
