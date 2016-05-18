import Data.List (lookup)
import Data.Char (toLower)

main = do
  contents <- getContents
  let program = (map words . lines) contents
  go program []

go :: [[String]] -> [(String, Int)] -> IO ()
go [] _         = return ()
go (x:xs) state = do
  let (command:args) = x
  if command == "define"
     then go xs ((unwords $ tail args, read $ head args):state)
     else do let (lvar, rest) = break ((`elem` "><=").head) args
             let (op, rvar) = (head rest, unwords $ tail rest)
             let (lval, rval) = (lookup (unwords lvar) state, lookup rvar state)
             case (lval, rval) of (Nothing, _) -> putStrLn "undefined"
                                  (_, Nothing) -> putStrLn "undefined"
                                  (Just l, Just r) -> putStrLn $ (map toLower) $ case op of "<" -> show $ l < r
                                                                                            ">" -> show $ l > r
                                                                                            "=" -> show $ l == r
             go xs state
