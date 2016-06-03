import Data.Set (Set)
import qualified Data.Set as Set
import Text.Printf

main = do
  cards <- getLine
  case sortCards cards of Left str -> putStrLn str
                          Right (p, k, h, t) -> printf "%d %d %d %d\n" (13 - Set.size p) (13 - Set.size k) (13 - Set.size h) (13 - Set.size t)
  
sortCards :: String -> Either String (Set String, Set String, Set String, Set String)
sortCards [] = Right (Set.empty, Set.empty, Set.empty, Set.empty)
sortCards (x:y:z:xs) = let card = x:y:z:"" in case x of
    'P' -> case sortCards xs of Left str -> Left str
                                Right (p, k, h, t) -> if Set.member card p
                                                         then Left "GRESKA"
                                                         else Right ((Set.insert) card p, k, h, t)
    'K' -> case sortCards xs of Left str -> Left str
                                Right (p, k, h, t) -> if Set.member card k
                                                         then Left "GRESKA"
                                                         else Right (p, (Set.insert) card k, h, t)
    'H' -> case sortCards xs of Left str -> Left str
                                Right (p, k, h, t) -> if Set.member card h
                                                         then Left "GRESKA"
                                                         else Right (p, k, (Set.insert) card h, t)
    'T' -> case sortCards xs of Left str -> Left str
                                Right (p, k, h, t) -> if Set.member card t
                                                         then Left "GRESKA"
                                                         else Right (p, k, h, (Set.insert) card t)
