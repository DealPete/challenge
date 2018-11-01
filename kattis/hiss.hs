main = do
  line1 <- getLine
  putStrLn $ case hiss line1 of
    True -> "hiss"
    False -> "no hiss"

hiss :: String -> Bool
hiss [] = False
hiss (x:xs)
  | x == 's' = hisss xs
  | otherwise = hiss xs

hisss :: String -> Bool
hisss [] = False
hisss (x:xs)
  | x == 's' = True
  | otherwise = hiss xs
