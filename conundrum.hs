main = do
  line1 <- getLine
  print $ length $ filter (\(a, b) -> a /= b) (zip line1 (cycle "PER"))