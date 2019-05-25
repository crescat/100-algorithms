import Debug.Trace
import Data.Function
import Text.Printf

import Data.Function.Memoize

type MatSize = (Integer, Integer)

--         len      l    r       total multOpCount
-- memoize :: Int -> ((Int, Int) -> Integer) -> ((Int, Int) -> Integer)
-- memoize len f (l,r) = (map (f . decode) [0..]) !! (encode (l,r))
--   where encode (l,r) = len * l + r
--         decode i = i `divMod` len

mcm' :: [MatSize] -> ((Int, Int) -> Integer) -> ((Int, Int) -> Integer)
mcm' ms f (a,b)
  | a == b     = 0
  | otherwise  = minimum $ map mcmAtCut [a..b-1]
    where mcmAtCut i = f (a,i) + f (i+1,b) + costAtCut i
          costAtCut i = multOpCount (shape a i) (shape (i+1) b)
          shape l r = multShape (take (r-l+1) $ drop l ms)

mcm'' :: [MatSize] -> (Int, Int) -> Integer
mcm'' ms (a,b)
  | a == b     = 0
  | otherwise  = minimum $ map mcmAtCut [a..b-1]
    where mcmAtCut i = mcm'' ms (a,i) + mcm'' ms (i+1,b) + costAtCut i
          costAtCut i = multOpCount (shape a i) (shape (i+1) b)
          shape l r = multShape (take (r-l+1) $ drop l ms)

mcm :: [MatSize] -> Integer
mcm ms = fix (mcm' ms) (0, length ms - 1)

memoizedMcm :: [MatSize] -> Integer
memoizedMcm ms = memoize2 mcm'' ms (0, length ms - 1)
  where len = length ms

multShape :: [MatSize] -> MatSize
multShape [] = error "no mult size for no mat"
multShape xs = (fst $ head $ xs, snd $ last $ xs)

multOpCount :: MatSize -> MatSize -> Integer
multOpCount (a,b) (_c,d) = a * d * b


main = do
  let mat = zip [1..20] [2..]
  -- print $ fromIntegral $ mcm mat
  print $ fromIntegral $ memoizedMcm mat

  let mat = zip [1..20] [2..]
  print $ fromIntegral $ memoizedMcm mat



