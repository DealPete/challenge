import Control.Monad

main = do
  numCases <- getLine
  replicateM_ (read numCases) go

go = do
  recordings <- getLine
  sounds <- getSounds
  let soundMap = map ((\[animal, _, sound] -> (sound, animal)).words) sounds
  putStrLn $ unwords $ filter (\x -> lookup x soundMap == Nothing) (words recordings)

getSounds :: IO [String]
getSounds = do
  sound <- getLine
  if sound == "what does the fox say?"
     then return []
     else do sounds <- getSounds
             return (sound : sounds)
