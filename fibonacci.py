#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

#validate and return user input
def getuserinput():
  while true
    t = int(input("Enter number of terms for Fibonacci sequence: ))
    if  t <= 0:
      print("Please enter postive integer")
    else:
       return t
        except ValueError:
      print("Invalid! Please enter an integer")

def generate_fibonacci(c):
sequence = []
x,y = 0,1
for i in range(c)
  sequence.append(x)
  x,y = y, x + y
  return sequence

def print_sequence():
  print("Fibonacci Sequence:")

def main():
count = getuserinput()          # Step 1: Get user input (validated)
fibonacci_seq = generate_fibonacci(count)  # Step 2: Generate Fibonacci sequence
print_sequence(fibonacci_seq)           # Step 3: Print the sequence
  
  



                  
    
