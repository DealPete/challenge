main = do
  line1 <- getLine
  let [r1, s] = map read (words line1)
  putStrLn $ show $ s * 2 - r1
