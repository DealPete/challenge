import System.Environment
import Data.List (intercalate)
import Control.Monad

main :: IO ()
main = go 1

go :: Int -> IO()
go i = do
  n <- getLine
  if n == "0"
    then return ()
    else do putStrLn ("SET " ++ show i)
            process (read n)
            go (i + 1)

readInput :: String -> [String]
readInput = words

process :: Int -> IO ()
process n = do
  names <- replicateM n getLine
  mapM_ putStrLn (doSort names)

doSort :: [String] -> [String]
doSort [] = []
doSort [x] = [x]
doSort (x:y:xs) = [x] ++ doSort xs ++ [y]