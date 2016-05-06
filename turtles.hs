import Control.Monad

main = do
  line1 <- getLine
  lines <- replicateM (read line1) getLine
  let turtles = map ((map read).init.words) lines
  mapM_ (putStrLn.show.fst.(foldl next (0, 1))) turtles

next :: (Int, Int) -> Int -> (Int, Int)
next (acc, prev) x
  | x > 2*prev = (x - 2*prev + acc, x)
  | otherwise  = (acc, x)
