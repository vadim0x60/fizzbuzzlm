#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void fizzbuzz(char* fb, int i) {
  sprintf(fb, "%s%s", i%3 ? "" : "Fizz", i%5 ? "" : "Buzz");
  if (fb[0] == '\0') sprintf(fb, "%d", i); 
}

int main() {
  char fb[9];
  for (int i=1; i<=100; i++) {
    fizzbuzz(fb, i);
    printf("%s\n", fb);
  }
  return 0;
}