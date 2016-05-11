main = do
  reps <- getLine
  lineA <- getLine
  lineB <- getLine
  let reps' = read reps
  if reps' `mod` 2 == 0
     then if lineA == lineB
             then putStrLn "Deletion succeeded"
             else putStrLn "Deletion failed"
     else if map toggle lineA == lineB
             then putStrLn "Deletion succeeded"
             else putStrLn "Deletion failed"

toggle '1' = '0'
toggle '0' = '1'
