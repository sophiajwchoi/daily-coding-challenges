gcdd:: Int -> Int -> Int
gcdd a b
    | a > b = gcdd (a - b) b
    | a < b = gcdd (b - a) a
    | otherwise = a 

isPrime :: Int -> Bool
isPrime a = 

coprime :: Int -> Int -> Bool
coprime a b = isPrime a && isPrime b

totient :: Int -> Int
totient a = 
    do x <- [1..x]
        a = 0
        if (isPrime x)

        return  
---from 1 to x counts the Prime number  returns the count

counter :: Int
counter a = a + 1;