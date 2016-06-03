main = do
  sets <- getLine
  interact (unlines . (map process) . lines)

process :: String -> String
process datums =
  let nums = (map read).words $ datums in
      unwords [show $ head nums, show $ go [] (tail nums)]

go :: [Int] -> [Int] -> Int
go _ [] = 0
go ls (x:xs) = let (smaller, larger) = span (<x) ls in
                   length larger + go (smaller ++ [x] ++ larger) xs
