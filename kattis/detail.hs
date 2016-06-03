import Control.Monad

main = do
  cases <- getLine
  replicateM_ (read cases) process
  
process :: IO ()
process = do
  line1 <- getLine
  line2 <- getLine
  putStrLn line1
  putStrLn line2
  putStrLn $ foldr (\(a, b) acc -> (if a == b then '.' else '*'):acc) [] (zip line1 line2)
  putStrLn ""