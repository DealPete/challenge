import Kattis (matrixify)
import Control.Monad
import Data.List (transpose)

main = do
  line <- getLine
  lines <- replicateM (read line) getLine
  mapM_ process lines

process :: String -> IO ()
process phrase = do
  let dim = head $ dropWhile ((<(length phrase)).(^2)) [1..]
  let matrix = matrixify dim phrase
  putStrLn $ reverse $ concat $ transpose $ reverse matrix
