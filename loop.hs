import Data.List (sort, partition)
import Text.Printf

main = do
  cases <- getLine
  go 1 (read cases)

go :: Int -> Int -> IO ()
go i n = do
  printf "Case #%d:" i
  segments <- getLine
  lengths <- getLine
  let (redStrs, blueStrs) = partition ((=='B').last) (words lengths)
  let reds = reverse $ sort $ map (read.init) redStrs
  let blues = reverse $ sort $ map (read.init) blueStrs
  let loop = zip reds blues
  printf " %d\n" (foldl (\acc (red, blue) -> acc + red + blue) 0 (loop) - 2*length loop)
  if i == n
     then return ()
     else go (i+1) n
  
