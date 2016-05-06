import Control.Monad
import Data.Time
import Data.Time.Clock.POSIX
import Text.Regex

parse :: String -> Int
parse str = read year
	where Just [year, month, day] = matchRegex (mkRegex "(.*)/(.*)/(.*)") str
	 
	 
main :: IO ()
main = do
	n <- getLine
	replicateM_ (read n) process
	
process :: IO ()
process = do
	str <- getLine
	let [name, beginYear, birthYear, courses] = words str in
		if (parse beginYear > 2009) then
			putStrLn (name ++ " eligible")
		else
			if (parse birthYear > 1990) then
				putStrLn (name ++ " eligible")
			else
				if (read courses > 40) then
					putStrLn (name ++ " ineligible")
				else
					putStrLn (name ++ " coach petitions")
			
	