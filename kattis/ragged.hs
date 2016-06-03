main = do
  paragraph <- getContents
  let lengths = map length (lines paragraph)
  let n = maximum lengths
  print $ sum $ map (\m -> (n - m)^2) (init lengths)
