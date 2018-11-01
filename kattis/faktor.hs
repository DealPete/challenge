main = do
  line <- getLine
  let [a, i] = map read (words line)
  putStrLn $ show $ a * i - ((a * i - 1) `mod` a)
