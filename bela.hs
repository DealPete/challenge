dom = [('A', 11), ('K', 4), ('Q', 3), ('J', 20), ('T', 10), ('9', 14), ('8', 0), ('7', 0)]
nonDom = [('A', 11), ('K', 4), ('Q', 3), ('J', 2), ('T', 10), ('9', 0), ('8', 0), ('7', 0)]

main = do
  line <- getLine
  let [_, trump] = words line
  contents <- getContents
  let cards = words contents
  print $ foldl (sumCards trump) 0 cards

sumCards trump acc card
  | tail card == trump = acc + maybe 0 id (lookup (head card) dom)
  | otherwise          = acc + maybe 0 id (lookup (head card) nonDom)
