numeros=[]
def verificaInput(numero):
    while True:
        try:
            numeroC=float(numero)
            numeros.append(numeroC)
            break
        except ValueError:
             numero=input("Número inválido. Digite novamente ")
         
executando='S'

while executando=='S':
    num1=input("Insira o primeiro número ")
    verificaInput(num1)
    num2=input("Insira o segundo número ")
    verificaInput(num2)

    operadores={'soma':'+',
            'subtração':'-',
            'multiplicação':'*',
            'divisão':'/'}

    for indice, (nomeOperacao, operador) in enumerate(operadores.items()):
        if operador=='+':
            operacao=numeros[0]+numeros[1]
        elif operador=='-':
            operacao=numeros[0]-numeros[1]
        elif operador=='*':
            operacao=numeros[0]*numeros[1]
        elif operador=='/' and numeros[1]!=0:
            operacao=numeros[0]/numeros[1]
        else:
            print('Operação de divisão por zero é inválida')
            break
        print(f'A {nomeOperacao} é igual a {operacao}')
    numeros=[]
    executando=input('Deseja fazer nova operação? Digite S para continuar e N para parar')