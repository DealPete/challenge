import Text.Printf
import Challenge (fibs)

main = do
  line <- getLine
  let presses = read line
  printf "%d %d" (fibo $ presses - 1) (fibo $ presses)

fibo n = head $ drop n (0:fibs)
