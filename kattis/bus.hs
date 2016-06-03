import Control.Monad

main = do
  line <- getLine
  cases <- replicateM (read line) getLine
  mapM_ (\n -> print $ 2^n - 1) (map read cases)
