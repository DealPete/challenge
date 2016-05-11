import Data.Char (isDigit)
import Text.Printf

main = do
  interact (unlines . map processLine . lines) 

processLine :: String -> String
processLine lineRaw = do
  let line = words lineRaw
  let (name, values) = (filter (\(x:xs) -> not $ isDigit x) line,
                        filter (\(x:xs) -> isDigit x) line)
  show ((sum.map read) values / fromIntegral (length values)) ++ " " ++ unwords name
   
