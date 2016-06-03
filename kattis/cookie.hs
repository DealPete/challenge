main = do
  interact (unlines . map process . lines)

process :: String -> String
process input = do
  let [r, x, y] = (map read).words $ input
  let a = sqrt (x^2 + y^2)
  if a > r
     then "miss"
     else do let theta = acos (a/r)
             let l = r * sin theta
             let smaller = r^2 * theta - a*l
             let larger = pi*r^2 - smaller
             show larger ++ " " ++ show smaller

