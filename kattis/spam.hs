import Data.Char (ord)

data Symbol = Whitespace | Lower | Upper | Symbol
  deriving Eq

symbolType :: Char -> Symbol
symbolType c
  | c == '_' =            Whitespace
  | c `elem` ['a'..'z'] = Lower
  | c `elem` ['A'..'Z'] = Upper
  | otherwise =           Symbol 

main = do
  email <- getLine
  let freqs = map symbolType email
  print $ (fromIntegral $ length $ filter (==Whitespace) freqs)/(fromIntegral $ length freqs)
  print $ (fromIntegral $ length $ filter (==Lower) freqs)/(fromIntegral $ length freqs)
  print $ (fromIntegral $ length $ filter (==Upper) freqs)/(fromIntegral $ length freqs)
  print $ (fromIntegral $ length $ filter (==Symbol) freqs)/(fromIntegral $ length freqs)
