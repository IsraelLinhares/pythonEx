num = int(input('digite em que horas começou:'))
num1 = int(input('digite em que minutos começou:'))
num2 = int(input('digite em que segundos começou:'))
time = int(input('quantos segundos durou:'))
if time<59-num2:
    print(f'começou em {num}:{num1}:{num2}')
    print(f'terminou em {num}:{num1}:{num2 + time}')
