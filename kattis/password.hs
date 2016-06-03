main = do
  line <- getLine
  let [password, message] = words line
  putStrLn $ check password message

check :: String -> String -> String
check [] _ = "PASS"
check _ [] = "FAIL"
check (x:xs) (y:ys) = if x == y
  then check xs ys
  else if y `elem` xs
          then "FAIL"
          else check (x:xs) ys
