
type Grid = [[Int]]

main :: IO ()
main = do
  let 
    grid = 
      [ [1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0]
      , [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
      , [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0]
      , [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0]
      , [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0]
      , [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
      , [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
      , [0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1]
      , [0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0]
      , [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1]
      , [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0]
      , [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
      , [0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,1,0,0]
      , [1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0]
      , [0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0]
      , [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
      , [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
      , [0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0]
      , [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
      , [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      ] :: [[Int]]
  loop grid

loop :: Grid -> IO ()
loop grid = do
  getLine
  let adjacencies = map (map (uncurry (countAdjacent grid))) [[(i, j) | j <- [0..59]] | i <- [0..59]]
  let grid' = map (map maze) $ zipWith zip grid adjacencies
  print' grid'
  loop grid'

print' :: Grid -> IO ()
print' grid = do
  putStrLn $ replicate 22 '#'
  mapM_ (putStrLn . (\x -> "#" ++ concatMap convert x ++ "#") . concatMap show) grid
  putStrLn $ replicate 22 '#'

maze :: (Int, Int) -> Int
maze (current, adjacent)
  | adjacent < 2 = 0
  | (adjacent == 2 || adjacent == 3) && current == 1 = 1
  | adjacent == 3 = 1

countAdjacent :: Grid -> Int -> Int -> Int
countAdjacent grid i j = sum $ getAdjacent grid i j

getAdjacent :: Grid -> Int -> Int -> [Int]
getAdjacent grid i j = [grid !! a !! b | a <- [i-1, i, i+1], b <- [j-1, j, j+1], (a /= i || b /= j) && a >= 0 && a <= ilen && b >= 0 && b <= jlen]
  where
    ilen = length grid - 1
    jlen = length (grid !! i) - 1

convert :: Char -> String
convert '0' = "  "
convert '1' = "██"