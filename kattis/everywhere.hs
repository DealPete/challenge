import Data.List (nub)
import Control.Monad

main :: IO ()
main = do
	n <- getLine
	replicateM_ (read n) process

process :: IO ()
process = do
	n <- getLine
	cities <- replicateM (read n) getLine
	putStrLn $ show $ length $ nub cities