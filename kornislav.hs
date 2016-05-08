import Data.List (sort)

main = do
  nums <- getLine
  let [a, b, c, d] = sort $ map read $ words nums
  print (a * c)
