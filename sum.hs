main = do
  interact (unlines . map process . lines)

process line =
  let ints = (map read . words) line in
  show $ head $ dropWhile (\a -> a /= sum ints - a) ints
