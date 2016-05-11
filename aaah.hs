main = do
  jon <- getLine
  doctor <- getLine
  if length jon < length doctor
     then putStrLn "no"
     else putStrLn "go"
