import Text.Printf
import Data.List (group, sort)

main = do
  testsRaw <- getLine
  mapM_ process [1..(read testsRaw)]

process :: Int -> IO ()
process n = do
  guests <- getLine
  ids <- getLine
  printf "Case #%d: %s\n" n
    (head $ head $ dropWhile ((/=1).length) (group $ sort (words ids))) 
