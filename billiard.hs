import Text.Printf

main = do
  line <- getLine
  if line == "0 0 0 0 0"
     then return ()
     else do let [a, b, s, m, n] = (map read).words $ line
             let angle = (180/pi) * atan (n*b/(m*a)) :: Float
             let speed = (1/s) * sqrt (m^2*b^2 + n^2*a^2) :: Float
             printf "%f %f\n" angle speed
             main