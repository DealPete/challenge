import Text.Printf

main = do
  tile <- getLine
  printf "%d %d %d\n" (length tile) (foldl xfold 0 tile) (foldl yfold 0 tile)

xfold :: Int -> Char -> Int
xfold acc x = if x == '1' || x == '3' then 1 + 2*acc else 2*acc

yfold :: Int -> Char -> Int
yfold acc x = if x == '2' || x == '3' then 1 + 2*acc else 2*acc
