import Text.Printf

main = do
  problems <- readInput
  let (solved, score) = solve $ map (tuplify.words) problems
  printf "%d %d\n" (length solved) score

tuplify :: [String] -> (Int, Char, String)
tuplify [a, b, c] = (read a, head b, c)

readInput :: IO [String]
readInput = do
  line <- getLine
  if line == "-1"
     then do return [] 
     else do lines <- readInput
             return $ line:lines
 
solve :: [(Int, Char, String)] -> ([Char], Int)
solve [] = ([], 0)
solve ((t, prob, success):xs) = let (solved, score) = solve xs in
                                    if success == "right"
                                       then (prob:solved, score + t)
                                       else if prob `elem` solved
                                               then (solved, score + 20)
                                               else (solved, score)
