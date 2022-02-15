
salario = int(input('digite o seu salário: '))
emprestimo = int(input('digite o valor da prestação do empréstimo: '))


if emprestimo < salario*0.2:
    print('empréstimo concedido')

else:
    print('empréstimo não concedido')

