filter' :: (a -> Bool) -> [a] -> [a]  
filter' _ [] = []  
filter' p (x:xs)   
    | p x       = x : filter' p xs  
    | otherwise = filter' p xs  

map' :: (a -> b) -> [a] -> [b]  
map' _ [] = []  
map' f (x:xs) = f x : map' f xs  

squareSingleDigitNumbers x = map' (^2) (filter' (<10) x)

main = print(squareSingleDigitNumbers [2, 7, 15, 11, 5])