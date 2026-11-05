# print('Inicio')
# assert 1 > 0
# print('fim')

# try:
#     idade = int(input("Digite sua idade: "))
# except:
#     print('Digite somente números inteiros')
    
try: 
    n1 = int(input("Digite sua idade: "))
    n2 = int(input("Digite sua idade: "))
    resultado = n1 / n2
    print("O resultado é", resultado)
except ValueError:
    print("Digite somente números inteiros")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")