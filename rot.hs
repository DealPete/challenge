code = cycle "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

main = do
  line <- getLine
  if line == "0"
    then return ()
    else do
      let [n, word] = words line
      putStrLn $ map (rot (read n)) (reverse word)
      main

rot :: Int -> Char -> Char
rot n c = dropWhile (/=c) code !! n
