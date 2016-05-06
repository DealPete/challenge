import Text.Printf
import Control.Monad

main = do
    lines <- replicateM 3 getLine
    let [[x1, y1], [x2, y2], [x3, y3]] = map words lines
    let
        (x4, y4) = if x1 == x2
            then if y1 == y3
                then (x3, y2)
                else (x3, y1)
            else if x2 == x3
                then if y1 == y2
                    then (x1, y3)
                    else (x1, y2)
                else if y1 == y2
                    then (x2, y3)
                    else (x2, y1)
    printf "%s %s" x4 y4
			