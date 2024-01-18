(defn fizz-buzz [n]
  (or (not-empty (str 
        (if (zero? (mod n 3)) "Fizz") 
        (if (zero? (mod n 5)) "Buzz")))
      (str n)))

(println (map fizz-buzz (range 1 101)))