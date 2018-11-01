import Data.List.Split (splitOn)

main = do
  line1 <- getLine
  putStrLn $ map head $ splitOn "-" line1
