import Text.Printf

main = do
  interact (unlines . process . lines)

process strings = map go (zip strings [1..])

go :: (String, Int) -> String
go (line, i) =
  let input = tail $ (map read . words) line :: [Int] in
  let min = minimum input in
  let max = maximum input in
  let range = max - min in
  printf "Case %d: %d %d %d" i min max range
