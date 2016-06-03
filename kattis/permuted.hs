import Control.Monad
import Data.List (sort)

main = do
  numLines <- getLine
  lines <- replicateM (read numLines) getLine
  mapM_ process lines

process :: String -> IO ()
process line = do
  let ints = (map read . tail . words) line
  let diffs = differences ints
  if all (==head diffs) diffs
     then putStrLn "arithmetic"
     else let difs = differences (sort ints) in
              if all (==head difs) difs
                 then putStrLn "permuted arithmetic"
                 else putStrLn "non-arithmetic"

differences :: [Int] -> [Int]
differences ints = map (uncurry (-)) (zip (tail ints) ints)

