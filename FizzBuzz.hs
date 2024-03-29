-- This program is unapologetically copied from Rosetta Code.
-- http://rosettacode.org/wiki/FizzBuzz#Haskell
main = mapM_ (putStrLn . fizzbuzz) [1..100]

fizzbuzz n = 
    show n <|> [fizz| n `mod` 3 == 0] ++ 
               [buzz| n `mod` 5 == 0]

infixr 0 <|>
d <|> [] = d
_ <|> x = concat x

fizz = "Fizz"
buzz = "Buzz"