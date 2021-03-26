fib :: (Integral a) => a -> a 
fib 0 = 0
fib 1 = 1
fib n = fib(n -1) + fib(n -2)

firstKEntriesOfSequence k = [0..k]

termsToAddInMetaSum n =map fib (firstKEntriesOfSequence n)

fiboffibs n = map termsToAddInMetaSum (termsToAddInMetaSum n)

fibSum n = map sum(fiboffibs n)
metaSum n = sum (fibSum n)


main = print(metaSum 6)
