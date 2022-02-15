
from math import sqrt


num1 = int(input('digite um numero: '))

if num1 > 0:
    print(f'a raiz quadrada desse numero: {sqrt(num1)}')
else:
    print(f'o quadrado desse numero: {num1**2}')