import Control.Monad

main = do
  prices <- getLine
  let priceMap = 0 : ((map read) . words $ prices) 
  parkTimes <- replicateM 3 getLine
  let parkTimeInts = map ((map read). words) parkTimes
  let parkings = map (\time -> length $ filter (\[startTime, endTime] -> time >= startTime && time < endTime) parkTimeInts) [1..100]
  print $ sum $ map (\trucks -> trucks * (priceMap !! trucks)) parkings
