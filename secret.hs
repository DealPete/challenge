main = do

matrixify :: Int -> [a] -> [[a]]
matrixify _ [] = [[]]
matrixify n ls = take n ls : matrixify (drop n ls)
