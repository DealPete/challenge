import Data.List (sort, nub)
import Control.Monad

main = do
  contents <- getContents
  let atoms = words contents
  let compounds = nub $ sort $ map concat [[a,b]| a <- atoms, b <- atoms, a /= b]
  mapM_ putStrLn compounds
