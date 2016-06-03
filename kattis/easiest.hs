import Challenge (digitSum)

main = do
    line <- getLine
    if read line == 0 then
        return ()
    else do
        putStrLn $ show $ smallest $ read line
        main

smallest :: Int -> Int
smallest k = head $ dropWhile (\num -> digitSum (k*num) /= digitSum k) [11..]
