import Data.Maybe (fromJust)
import Data.List 
import Control.Monad

main = do
  line <- getLine
  if line == "0"
     then return ()
     else go $ read line

go :: Int -> IO ()
go n = do
  list1 <- replicateM n getLine
  list2 <- replicateM n getLine
  let (listA, listB) = (map read list1, map read list2) :: ([Int], [Int])
  let [sortA, sortB] = [sort listA, sort listB]
  let finalB = map (\(x, _) -> sortB !! (fromJust $ elemIndex x sortA)) $ zip listA listB
  mapM_ print finalB
  line <- getLine
  if line == "0"
     then return ()
     else do putStrLn ""
             go $ read line
