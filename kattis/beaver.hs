main = do
  line <- getLine
  if line == "0 0"
     then return ()
     else do let [vD, vV] = (map read . words) line :: [Double]
             print $ (vD^3 - 6*vV/pi)**(1/3)
             main
