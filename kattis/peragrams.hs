import Data.List (sort, group)

main = do
  word <- getLine
  let lengths = map length . group . sort $ word
  let total = length (filter odd lengths) - 1
  if total < 0
     then print 0
     else print total
