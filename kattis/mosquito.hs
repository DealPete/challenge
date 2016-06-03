import Control.Monad

main = do
  input <- getContents
  mapM_ (process . words) (lines input)

process :: [String] -> IO ()
process ints = do
  let [m, p, l, e, r, s, n] = map read ints
  print $ head $ iterate (lifecycle e r s) [m, p, l] !! n
  
  
lifecycle e r s [m, p, l] = [p `div` s, l `div` r, m*e]
