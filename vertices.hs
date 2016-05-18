import Data.List
import Control.Monad

main = do
  line <- getLine
  let numVertices = read line
  if numVertices == -1
     then return ()
     else do rawMatrix <- replicateM numVertices getLine
             let matrix = map (map read . words) rawMatrix
             let adj = map (map fst . filter ((/=0).snd) . zip [0..(numVertices - 1)]) matrix
             let nonTrigs = filter (notTrig adj) [0..(numVertices - 1)]
             putStrLn $ (unwords . map show) nonTrigs
             main

notTrig :: [[Int]] -> Int -> Bool
notTrig adj vertex =
  not $ any (\[v1,v2] -> v2 `elem` (adj !! v1)) (filter ((==2).length) (subsequences (adj !! vertex)))
