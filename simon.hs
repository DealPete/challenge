import Control.Monad
import Text.Regex.Posix

main = do
  line1 <- getLine
  lines <- replicateM (read line1) getLine
  mapM_ putStrLn $ (map (drop 11).filter (=~"^Simon says")) lines

