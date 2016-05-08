import Text.Printf

main = do
  input <- getLine
  if input == "0 0 0"
    then return ()
    else do
      let [r, m, c] = (map read $ words input)
      process r m c
      main

process :: Double -> Double -> Double -> IO ()
process r m c = printf "%f %f\n" (pi * r^2) ((2*r)^2 * (c/m))
