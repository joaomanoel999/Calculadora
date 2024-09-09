n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))

opc = int(input("1- Adição 2-subtração 3- multiplicação 4 - divisão "))

if opc == 1:
    soma = n1 + n2
    print(soma)
elif opc == 2:
    subtração = n1 - n2
    print(subtração)

elif opc == 3:
    multiplica = n1 * n2
    print(multiplica)


elif opc == 4:    
    divisao = n1 / n2
    print(divisao)
print ("TCHAU OBRIGADO")
