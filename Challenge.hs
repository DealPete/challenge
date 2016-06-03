module Challenge where

import Data.Char (digitToInt)

digitSum :: Int -> Int
digitSum n = sum $ map digitToInt (show n)

fibs = 1:1:zipWith (+) fibs (tail fibs)

matrixify :: Int -> [a] -> [[a]]
matrixify _ [] = []
matrixify n ls = take n ls : matrixify n (drop n ls)

padTo :: Int -> a -> [a] -> [a]
padTo n el xs = xs ++ take (n - length xs) (repeat el)

