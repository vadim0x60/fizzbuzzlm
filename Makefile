all: FizzBuzzC FizzBuzz.class FizzBuzz.exe FizzBuzzGo FizzBuzzHaskell FizzBuzzRust charlm.pt
	hyperfine --warmup 3 './FizzBuzzC' './FizzBuzzGo' './FizzBuzzHaskell' './FizzBuzzRust' 'java FizzBuzz' 'python FizzBuzz.py' 'mono FizzBuzz.exe' 'node FizzBuzz.js' 'clojure FizzBuzz.clj' 'python infer_charlm.py cpu' 'python infer_charlm.py mps'

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
FizzBuzzRust:
	rustc -o FizzBuzzRust FizzBuzz.rs
charlm.pt:
	python train_charlm.py mps