main = do
  line <- getLine
  let [n, p, q] = (map read . words) line
  if even ((p + q) `div` n)
     then putStrLn "paul"
     else putStrLn "opponent"
