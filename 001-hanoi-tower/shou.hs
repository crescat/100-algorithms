hanoi :: Int -> [(Int, Int)]
hanoi n = hanoi' n 1 3 2

hanoi' :: Int -> Int -> Int -> Int -> [(Int, Int)]
hanoi' 0 _ _ _ = []
hanoi' n a b c = (hanoi' (n - 1) a c b) ++
                 [(a, b)] ++
                 (hanoi' (n - 1) c b a)

type Piles = ([Int], [Int], [Int])

runSteps :: Piles -> [(Int, Int)] -> Piles
runSteps piles [] = piles
runSteps piles ((from,to):steps) = runSteps piles'' steps
  where (piles', e) = remove from piles
        piles'' = add to piles' e
        remove 1 (a:as,bs,cs) = ((as,bs,cs), a)
        remove 2 (as,b:bs,cs) = ((as,bs,cs), b)
        remove 3 (as,bs,c:cs) = ((as,bs,cs), c)
        add 1 (as,bs,cs) a = (a:as,bs,cs)
        add 2 (as,bs,cs) b = (as,b:bs,cs)
        add 3 (as,bs,cs) c = (as,bs,c:cs)

main :: IO ()
main = do
  print steps
  print (runSteps piles steps)
  where n = 3
        steps = hanoi n
        piles = ([1..n], [], [])

