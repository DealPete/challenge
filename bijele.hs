import Data.List (intercalate)

main = do
    line <- getLine
    let pieces = map read (words line)
    putStrLn $ intercalate " " $ map (show.sub) $ zip [1, 1, 2, 2, 2, 8] pieces

sub :: (Int, Int) -> Int
sub (a, b) = a - b