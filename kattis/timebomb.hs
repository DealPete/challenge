import Data.List

asciiNums = ["**** ** ** ****",
             "  *  *  *  *  *",
             "***  *****  ***",
             "***  ****  ****",
             "* ** ****  *  *",
             "****  ***  ****",
             "****  **** ****",
             "***  *  *  *  *",
             "**** ***** ****",
             "**** ****  ****"]

main = do
  ascii <- getContents
  putStrLn $ case unpack $ lines ascii
                  of Nothing  -> "BOOM!!"
                     Just str -> if (read str) `mod` 6 == 0
                                    then "BEER!!"
                                    else "BOOM!!"

unpack :: [String] -> Maybe String 
unpack ["","","","",""] = Just ""
unpack numbers = case elemIndex (concat $ map (take 3) numbers) asciiNums
                      of Nothing -> Nothing
                         Just n  -> case unpack $ map (drop 4) numbers
                                         of Nothing  -> Nothing
                                            Just str -> Just (show n ++ str)
