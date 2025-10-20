#!/usr/bin/env python3

def get_positive_integer():
    n = input("Enter the number of terms: ")
    while not n.isdigit() or int(n) <= 0:
        print("Please enter positive integer.")
        n = input("Enter the number of terms: ")
    return int(n)

def fibonnaci_sequence(n):
    a, b = 0, 1
    sequence = []
    for i in range(n):
      sequence.append(a)
      a, b = b, a + b
    return sequence

def print_fibonnaci(sequence):
  for num in sequence:
    print (num, end=" ")
  print()
  
    
        
def main():
    n = get_positive_integer()
    print("Fibonnaci sequence:")
    print_fibonnaci(n)

main()
