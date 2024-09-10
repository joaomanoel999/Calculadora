n1 = int(input("digite um valor: "))
n2 = int(input("digite outro valor: "))

print("1- Adição 2-subtração 3- multiplicação 4 - divisão ")
opc = int(input("digite a opção: "))

while opc < 1 or opc > 4:
    print("digite a opção novamente! ")
    opc = int(input("digite a opção: "))
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
