import Control.Monad
import Data.Char (digitToInt)

morseTable = [('A', ".-"),
              ('B', "-..."),
              ('C', "-.-."),
              ('D', "-.."),
              ('E', "."),
              ('F', "..-."),
              ('G', "--."),
              ('H', "...."),
              ('I', ".."),
              ('J', ".---"),
              ('K', "-.-"),
              ('L', ".-.."),
              ('M', "--"),
              ('N', "-."),
              ('O', "---"),
              ('P', ".--."),
              ('Q', "--.-"),
              ('R', ".-."),
              ('S', "..."),
              ('T', "-"),
              ('U', "..-"),
              ('V', "...-"),
              ('W', ".--"),
              ('X', "-..-"),
              ('Y', "-.--"),
              ('Z', "--.."),
              ('_', "..--"),
              ('.', "---."),
              (',', ".-.-"),
              ('?', "----")]

inverseMorseTable = map (\(a, b) -> (b, a)) morseTable

main = do
  contents <- getContents
  let messages = lines contents
  mapM_ putStrLn (map go messages)

go :: String -> String
go msg = let (morse, nums) = encode msg in
  decode morse (reverse nums)

encode :: String -> (String, String)
encode "" = ("", "")
encode (x:xs) = (code ++ morseTail, (show $ length code) ++ numsTail)
  where (morseTail, numsTail) = encode xs
        code = maybe "" id (lookup x morseTable)

decode :: String -> String -> String
decode "" _ = ""
decode msg (n:ns) = maybe ' ' id (lookup (take (digitToInt n) msg) inverseMorseTable) : decode (drop (digitToInt n) msg) ns
