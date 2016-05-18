import Data.List

main = do
  line <- getLine
  numbers <- getLine
  let ints = (sort . map read . words) numbers
  let marks = map (\(a,b) -> (a, a - b)) (zip ints (0:ints))
  putStrLn $ unwords $ map shorten (formGroups marks)

formGroups :: [(Int, Int)] -> [[Int]]
formGroups [] = []
formGroups (x:xs) = (fst x : map fst (takeWhile ((==1).snd) xs)) : formGroups (dropWhile ((==1).snd) xs)

shorten :: [Int] -> String
shorten group = if length group > 2
                   then show (head group) ++ "-" ++ show (last group)
                   else if length group == 1
                        then show $ head group
                        else unwords $ map show group
