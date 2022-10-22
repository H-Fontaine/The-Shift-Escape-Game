import numpy as np

n = 10

def generate_code(n):
  sequence = ""

  for i in range(0, n):
    for j in range(0, i + 1):
        sequence += " -"
    sequence += "\n"
  return(sequence)

def generate_code2(n): return "" + "\n".join([' -'*i for i in range(1,n+1)]) + '\n'

(lambda __g, __operator, __y: [None for __g['generate_code'], generate_code.__name__ in [(lambda n: (lambda __l: [[(lambda __items, __after, __sentinel: __y(lambda __this: lambda: (lambda __i: [(lambda __items, __after, __sentinel: __y(lambda __this: lambda: (lambda __i: [[__this() for __l['sequence'] in [(__operator.iadd(__l['sequence'], ' -'))]][0] for __l['j'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(0, (__l['i'] + 1))), lambda: [__this() for __l['sequence'] in [(__operator.iadd(__l['sequence'], '\n'))]][0], []) for __l['i'] in [(__i)]][0] if __i is not __sentinel else __after())(next(__items, __sentinel)))())(iter(range(0, __l['n'])), lambda: __l['sequence'], []) for __l['sequence'] in [('')]][0] for __l['n'] in [(n)]][0])({}), 'generate_code')]][0])(globals(), __import__('operator', level=0), (lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))))


print(generate_code(n) == generate_code2(n))
print(generate_code2(n))
