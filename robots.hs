import Text.Printf
import Control.Monad

main = do
  dims <- getLine
  if dims == "0 0"
     then return ()
     else go dims
        
go dims = do
  line <- getLine
  lines <- replicateM (read line) getLine
  let lines' = map words lines
  let ((rtx, rty), (ax, ay)) = foldl (mapRobot $ (map read . words) dims) ((0, 0), (0, 0)) lines'
  printf "Robot thinks %d %d\n" rty rtx
  printf "Actually at %d %d\n" ay ax
  dims' <- getLine
  if dims' == "0 0"
     then return ()
     else do putStrLn ""
             go dims'

mapRobot :: [Int] -> ((Int, Int), (Int, Int)) -> [String] -> ((Int, Int), (Int, Int))
mapRobot [ydim, xdim] ((rtx, rty), (ax, ay)) [dir, dist] =
  let dist' = read dist in
  let rtx' = case dir of "d" -> rtx - dist'
                         "u" -> rtx + dist'
                         _   -> rtx in
  let rty' = case dir of "l" -> rty - dist'
                         "r" -> rty + dist'
                         _   -> rty in
  let ax' = case dir of "d" -> ax - dist'
                        "u" -> ax + dist'
                        _   -> ax in
  let ay' = case dir of "l" -> ay - dist'
                        "r" -> ay + dist'
                        _   -> ay in
  let ax'' = if ax' < 0
                then 0
                else if ax' >= xdim
                     then xdim - 1
                     else ax' in
  let ay'' = if ay' < 0
                then 0
                else if ay' >= ydim
                     then ydim - 1
                     else ay' in
  ((rtx', rty'), (ax'', ay''))
