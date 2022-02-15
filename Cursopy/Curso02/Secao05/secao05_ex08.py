
num1 = int(input('digite a nota 1: '))
num2 = int(input('digite a nota 2: '))


if num1 < 0 or num2 < 0:
    print('!!! nota invalida !!!')

else:
    print(f'media: {(num1 + num2) / 2}')
