main = do
  line <- getLine
  let n = read line
  print $ 2 ^ (2 * n) + 2 ^ (n + 1) + 1
