import Control.Monad

main = do
  cases <- getLine
  replicateM_ (read cases) go

go = do
  line1 <- getLine
  line2 <- getLine
  let days = (map read . words) line2
  print $ countFridays 1 days

countFridays :: Int -> [Int] -> Int
countFridays _ [] = 0
countFridays day (x:xs) = if day `mod` 7 == 1 && x >= 13
  then 1 + countFridays (day + x) xs
  else countFridays (day + x) xs
