
num = int(input('valor total: '  ))

print(f'o total a pagar com 10% de desconto é: {num-num*0.10}R$')
print(f'o valor de cada parcela, no parcelamento de 3X sem juros: {num//3}R$')
print(f'A comissão em venda a vista é: {(num-num*0.10)*0.05} R$')
print(f'A comissão em venda parcelada é: {num*0.05} R$')

