main = do
  radius <- getLine
  let r = read radius
  print $ pi*r^2
  print $ 2*r^2
