main = do
  line <- getLine
  let [x, y] = (map read . words) line
  if y == 1
     then if x == 0
             then putStrLn "ALL GOOD"
             else putStrLn "IMPOSSIBLE"
     else print $ fromIntegral x / (1 - fromIntegral y)
