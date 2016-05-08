import Control.Monad
import Data.List (sort)

main = do
  num <- getLine
  names <- replicateM (read num) getLine
  if names == (sort names)
    then putStrLn "INCREASING"
    else if names == (reverse $ sort names)
      then putStrLn "DECREASING"
      else putStrLn "NEITHER"
