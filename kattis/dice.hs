main = do
  gunnar <- getLine
  emma <- getLine
  let [ga1, gb1, ga2, gb2] = map read $ words gunnar
  let [ea1, eb1, ea2, eb2] = map read $ words emma
  let gunnarTotal = ((ga2 - ga1)/2) + ga1 + ((gb2 - gb1)/2) + gb1
  let emmaTotal = ((ea2 - ea1)/2) + ea1 + ((eb2 - eb1)/2) + eb1
  if gunnarTotal > emmaTotal
    then putStrLn $ "Gunnar"
    else if gunnarTotal < emmaTotal
      then putStrLn $ "Emma"
      else putStrLn $ "Tie"
