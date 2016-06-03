main = do
  line1 <- getLine
  line2 <- getLine
  let [n, t] = (map read . words) line1
  let times = (map read . words) line2
  print $ length $ takeWhile (<=t) (scanl1 (+) times)
