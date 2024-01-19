all: FizzBuzzC FizzBuzz.class FizzBuzz.exe FizzBuzzGo FizzBuzzHaskell charlm.pt
	time ./FizzBuzzC > /dev/null
	time ./FizzBuzzGo > /dev/null
	time ./FizzBuzzHaskell > /dev/null
	time java FizzBuzz > /dev/null
	time python FizzBuzz.py > /dev/null
	time mono FizzBuzz.exe > /dev/null
	time node FizzBuzz.js > /dev/null
	time clojure FizzBuzz.clj > /dev/null
	time python infer_charlm.py cpu > /dev/null
	time python infer_charlm.py mps > /dev/null

FizzBuzzC:
	gcc -o FizzBuzzC FizzBuzz.c
FizzBuzz.class:
	javac FizzBuzz.java
FizzBuzz.exe:
	csc FizzBuzz.cs
FizzBuzzHaskell:
	ghc FizzBuzz.hs -o FizzBuzzHaskell
FizzBuzzGo:
	go build -o FizzBuzzGo FizzBuzz.go 
charlm.pt:
	python train_charlm.py