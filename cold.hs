main = do
  ints <- getLine
  temps <- getLine
  putStrLn $ show $ length $ filter ((<0).read) (words temps)
