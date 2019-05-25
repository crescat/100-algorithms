
type MatSize = (Integer, Integer)

--          matrices     l      r      total multOpCount
memoize :: ([MatSize] -> (Int, Int) -> Integer) ->
           ([MatSize] -> (Int, Int) -> Integer)
memoize f ms (l,r) = (map (f ms . decode) [0..]) !! (encode (l,r))
  where len = length ms
        encode (l,r) = len * l + r
        decode i = i `divMod` len

mcm' :: ([MatSize] -> (Int, Int) -> Integer) ->
        ([MatSize] -> (Int, Int) -> Integer)
mcm' f ms (a,b)
  | a == b     = 0
  | a + 1 == b = multOpCount (ms !! a) (ms !! b)
  | otherwise  = minimum $ map mcmAtCut [a+1..b-1]
    where mcmAtCut i = f ms (a,i) + f ms (i+1,b) + cost i
          cost i = multOpCount (ms!!i) (ms!!(i+1))

mcm :: [MatSize] -> Integer
mcm [] = 0
mcm [m] = 0
mcm [a,b] = multOpCount a b
mcm ms = minimum $ map (subseqMcm ms) [1..(length ms-1)]

subseqMcm :: [MatSize] -> Int -> Integer
subseqMcm ms i = mcm left + mcm right + multOp
  where left  = take i ms
        right = drop i ms
        leftShape  = multShape left
        rightShape = multShape right
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



