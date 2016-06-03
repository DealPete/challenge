import Control.Monad

main = do
  line1 <- getLine
  line2 <- getLine
  nLines <- replicateM (read line2) getLine
  let players = cycle [1..8]
  let answers = map parse $ map words nLines
  putStrLn $ show $ head $ fst $ foldl next (drop (inLine line1) players, 0) answers

inLine :: String -> Int
inLine line = read line - 1

parse :: [String] -> (Int, Char)
parse [x, y] = (read x, head y)

next :: ([Int], Int) -> (Int, Char) -> ([Int], Int)
next (x:xs, time) (duration, answer) = if
  time + duration > 210 || answer /= 'T'
    then (x:xs, time + duration)
    else (xs, time + duration)
