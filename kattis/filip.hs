main = do
  line1 <- getLine
  let numbers = map (read.reverse) (words line1)
  putStrLn $ show $ maximum (numbers :: [Int])
