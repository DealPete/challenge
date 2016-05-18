import Control.Monad

main = do
  line1 <- getLine
  line2 <- getLine
  mapM_ (process line1) ((map read . words) line2)

process :: String -> Int -> IO ()
process line1 p = do
  let [a, b, c, d] = (map read . words) line1
  putStrLn $ if attacked a b p && attacked c d p
                then "both"
                else if attacked a b p || attacked c d p
                     then "one"
                     else "none"

attacked :: Int -> Int -> Int -> Bool
attacked a b p = ((p - 1) `mod` (a + b)) - a < 0
