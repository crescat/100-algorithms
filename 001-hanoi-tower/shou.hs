hanoi :: Int -> [(Int, Int)]
hanoi n = hanoi' n 1 3 2

hanoi' :: Int -> Int -> Int -> Int -> [(Int, Int)]
hanoi' 0 _ _ _ = []
hanoi' n a b c = (hanoi' (n - 1) a c b) ++
                 [(a, b)] ++
                 (hanoi' (n - 1) b c a)

printSteps :: [(Int, Int)] -> IO ()
printSteps [] = return ()
printSteps ((a,b):xs) = do
  print (a,b)
  printSteps xs

main :: IO ()
main = let n = 3
           steps = hanoi 3
       in printSteps steps
