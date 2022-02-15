
sex = input('digite o seu sexo: ').lower()
if sex != "mulher" and sex != "homem" :
    print('! ! digite entre homem e mulher ! !')
else:
    altura = int(input('digite a sua altura em centimetros: '))
    if sex == 'mulher':
        print(f'seu peso ideal é: {(62.1*(altura/100)) - 44.7}')
    else:
        print(f'seu peso ideal é: {(72.7*(altura/100)) - 58}')
