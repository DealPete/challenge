import Control.Monad

main = do
  line1 <- getLine
  line2 <- getLine
  let x = read line1
  let n = read line2
  nLines <- replicateM n getLine
  let megs = map read nLines
  putStrLn $ show $ x*n - sum megs + x
