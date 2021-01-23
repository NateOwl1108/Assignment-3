calcList n = lenth[[x,y] |x-y<= (x*y)/2,  (x*y)/2  <= x+y, x >=-n ,y<= n]
                

main = putStrLn(calcList 50)