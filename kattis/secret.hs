
import Challenge (padTo, matrixify)
import Control.Monad
import Data.List (transpose)

main = do
  line <- getLine
  lines <- replicateM (read line) getLine
  mapM_ process lines

process :: String -> IO ()
process phrase = do
  let dim = head $ dropWhile ((<(length phrase)).(^2)) [1..]
  let rawMatrix = matrixify dim phrase
  let matrix = init rawMatrix ++ [padTo dim '*' (last rawMatrix)]
  putStrLn $ filter (/='*') $ concat $ transpose $ reverse matrix