import Control.Monad
import Data.Char (toLower)

main = do
  n <- getLine
  lines <- replicateM (read n) getLine
  mapM_ process lines

process line = do
  let lowerLine = map toLower line
  let letters = filter (not . (`elem` lowerLine)) ['a'..'z']
  if length letters == 0
     then putStrLn "pangram"
     else putStrLn $ "missing " ++ letters
  
