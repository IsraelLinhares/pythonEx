
from math import sqrt


num1 = int(input('digite um numero: '))

if num1 > 0:
    print(f'o quadrado desse numero: {num1**2}')
    print(f'a raiz quadrada desse numero: {sqrt(num1)}')
else:
    print('esse numero é invalido!!')