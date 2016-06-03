import Control.Monad

main = do
  num <- getLine
  mins <- replicateM (read num) getLine
  let minutes = sum $ map (read.head) (map words mins)
  let seconds = sum $ map (read.last) (map words mins)
  let avg = seconds / (minutes * 60)
  if avg <= 1
     then putStrLn "measurement error"
     else print avg
