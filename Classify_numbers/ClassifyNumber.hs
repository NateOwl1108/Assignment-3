classifyNumber x = if x < 0 
then "negative" else "non-negative"
main = putStrLn(classifyNumber 5)