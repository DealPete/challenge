import Text.Printf

main = do
  line <- getLine
  let [a, b, c] = words line
  solve (read a) (read b) (read c)

solve :: Int -> Int -> Int -> IO ()
solve a b c
  | a == b + c     = printf "%d=%d+%d\n" a b c
  | a == b * c     = printf "%d=%d*%d\n" a b c
  | a == b - c     = printf "%d=%d-%d\n" a b c
  | a == b `div` c = printf "%d=%d/%d\n" a b c
  | a + b == c     = printf "%d+%d=%d\n" a b c
  | a * b == c     = printf "%d*%d=%d\n" a b c
  | a - b == c     = printf "%d-%d=%d\n" a b c
  | a `div` b == c = printf "%d/%d=%d\n" a b c
