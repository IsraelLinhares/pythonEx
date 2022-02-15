ap1 = int(input('digite a aposta 1: '))
ap2 = int(input('digite a aposta 2: '))
ap3 = int(input('digite a aposta 3: '))
premio = int(input('digite prêmio: '))

print(f'o premio para a primeira aposta seria: {(ap1/(ap1+ap2+ap3))*100 + premio}')
print(f'o premio para a segunda aposta seria: {(ap2/(ap1+ap2+ap3))*100 + premio}')
print(f'o premio para a primeira aposta seria: {(ap3/(ap1+ap2+ap3))*100 + premio}')

