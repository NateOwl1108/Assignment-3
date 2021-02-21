chain :: (Integral a) => a -> [a]  
chain 1 = [1]  
chain n  
    | even n =  n:chain (n `div` 2)  
    | odd n  =  n:chain (n*3 + 1)

chain_length n = length(chain n)

chain_leghts_less_than_n n = (takeWhile (<n) (map (chain_length) [1..]))

firstNumberWithChainLengthGreaterThan n = length (chain_leghts_less_than_n n) + 1

main = print(firstNumberWithChainLengthGreaterThan 15)
          