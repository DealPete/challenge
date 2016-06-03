import Control.Monad

main = do
  contents <- getContents
  let board = lines contents
  print $ foldl (\acc y -> acc + foldl (\acc x -> acc + legalMoves y x board) 0 [0..6]) 0 [0..6]

legalMoves :: Int -> Int -> [String] -> Int
legalMoves y x board = if (board !! y) !! x == 'o'
  then a + b + c + d
  else 0
      where
        a = peg (y-2) x (y-1) x board
        b = peg (y+2) x (y+1) x board
        c = peg y (x-2) y (x-1) board
        d = peg y (x+2) y (x+1) board

peg :: Int -> Int -> Int -> Int -> [String] -> Int
peg y x y' x' board
  | y < 0 || x < 0 = 0
  | y > 6 || x > 6 = 0
  | otherwise      = if (board !! y) !! x == '.' && (board !! y') !! x' == 'o'
                        then 1
                        else 0

