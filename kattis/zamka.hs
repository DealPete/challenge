import Challenge (digitSum)

main = do
  strl <- getLine
  strd <- getLine
  strx <- getLine
  let [l, d, x] = map read [strl, strd, strx]
  let n = head (dropWhile ((/=x).digitSum) [l..])
  let m = head (dropWhile ((/=x).digitSum) [d, d-1..])
  putStrLn $ show n
  putStrLn $ show m