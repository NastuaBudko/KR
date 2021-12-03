import numpy as np

file = open('text.txt', "x")

a = np.random.randint(-5, 29, size=(3, 6))

print(a)

file.write (repr(a) + '\n')

file.close
