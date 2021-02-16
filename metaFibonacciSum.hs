fib :: (Integral a) => a -> a 
fib 0 = 0
fib 1 = 1
fib n = fib(n -1) + fib(n -2)

firstKEntriesOfSequence k = [0..k]

termsToAddInMetaSum n =map fib (firstKEntriesOfSequence n)

main = print(termsToAddInMetaSum 8)
