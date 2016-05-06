main = do
  line <- getLine
  putStrLn $ foldr unDup "" line

unDup :: Char -> String -> String
unDup c "" = c:""
unDup c (x:xs) = if c==x then x:xs else c:x:xs
