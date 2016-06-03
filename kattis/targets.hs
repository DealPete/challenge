import Control.Monad

main = do
  numTargets <- getLine
  targets <- replicateM (read numTargets) getLine
  numShots <- getLine
  shots <- replicateM (read numShots) getLine
  mapM (processShot targets) shots

processShot :: [String] -> String -> IO ()
processShot targets shot = do
  let targetsHit = foldl (shotHit shot) 0 targets
  print targetsHit

shotHit :: String -> Int -> String -> Int 
shotHit shot acc target = do
  let [shotX, shotY] = (map read . words) shot
  let targetWords = words target
  if head targetWords == "rectangle"
     then do let [x1, y1, x2, y2] = (map read . tail) targetWords
             if shotX >= x1 && shotY >= y1 && shotX <= x2 && shotY <= y2
                then acc + 1
                else acc
     else do let [x, y, r] = (map read . tail) targetWords
             if sqrt ((shotX - x)^2 + (shotY - y)^2) <= r
                then acc + 1
                else acc
