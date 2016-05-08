import Text.Printf

main = do
  let (solved, score) = solve
  printf "%d %d" (length solve) score

solve :: ([Char], Int)
solve = do
  line <- getLine
