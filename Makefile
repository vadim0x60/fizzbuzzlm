all: FizzBuzzC FizzBuzzJava FizzBuzz.exe
	time ./FizzBuzzC
	time java FizzBuzz
	time python FizzBuzz.py
	time mono FizzBuzz.exe
	time ./FizzBuzzHaskell
	time node FizzBuzz.js
	time clojure FizzBuzz.clj

FizzBuzzC:
	gcc -o FizzBuzzC FizzBuzz.c
FizzBuzzJava:
	javac FizzBuzz.java
FizzBuzz.exe:
	csc FizzBuzz.cs
FizzBuzzHaskell:
	ghc FizzBuzz.hs -o FizzBuzzHaskell
FizzBuzzGo:
	go build FizzBuzz.go -o FizzBuzzGo
charlm.pt:
	python train_charlm.py