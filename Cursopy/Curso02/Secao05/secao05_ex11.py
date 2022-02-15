

num = input('digite um numero: ')
if int(num) < 0:
    print("! numero invalido !")
else:
    if len(num) < 3 or len(num) > 3:
        print("! use apenas 3 algarismos !")
    else:
         alg1 = (int(num[0:1]))
         alg2 = (int(num[1:2]))
         alg3 = (int(num[2:3])) 
     
         print(f'a soma dos seus algorismos é: {alg1 + alg2 + alg3}')



