main = do
  line1 <- getLine
  putStrLn $ if (odd $ read line1) then "Alice" else "Bob"
