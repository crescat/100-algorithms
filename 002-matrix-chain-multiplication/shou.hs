
type MatSize = (Integer, Integer)

mcm :: [MatSize] -> Integer
mcm [] = 0
mcm [m] = 0
mcm [a,b] = multOpCount a b
mcm ms = minimum $ map (subseqMcm ms) [1..(length ms-1)]

subseqMcm :: [MatSize] -> Int -> Integer
subseqMcm ms i = leftMcm + rightMcm + multOp
  where left = take i ms
        right = drop i ms
        leftShape = multShape left
        rightShape = multShape right
        leftMcm = mcm left
        rightMcm = mcm right
        multOp = multOpCount leftShape rightShape


multShape :: [MatSize] -> MatSize
multShape [a] = a
multShape xs = let (a,b) = head xs
                   (c,d) = last xs
               in (a,d)

multOpCount :: MatSize -> MatSize -> Integer
multOpCount (a,b) (_c,d) = a * d * b


main = do
  let mat = [(10,20), (20,30), (30,40)]
  print $ mcm mat



