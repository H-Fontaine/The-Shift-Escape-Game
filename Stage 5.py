import numpy as np

n = 10

def generate_code(n):
  sequence = ""

  for i in range(0, n):
    for j in range(0, i + 1):
        sequence += " -"
    sequence += "\n"
  return(sequence)

test = '\n'.join([' -'*i for i in range(1,n+1)]) + '\n'
print(test == generate_code(n))
print(generate_code(n))