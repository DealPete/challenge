main = do
  line <- getLine
  if line == "0"
        then return ()
        else do let [x1, y1, x2, y2, p] = (map read . words) line
                print $ (abs (x1 - x2)**p + abs (y1 - y2)**p) ** (1/p)
                main
