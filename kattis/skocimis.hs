main = do
  line <- getLine
  let [a, b, c] = (map read).words $ line
  let (ba, cb) = (b - a, c - b)
  if cb > ba
     then print $ cb - 1
     else print $ ba - 1
