def printarTela():
    print("***************** Python Calculator *****************\n")
    print("Selecione o número da opção desejada:\n")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")
    return;

def captarDados():
    controle = input("Digite sua opção (1/2/3/4): ")
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    return[controle, num1, num2]

def calcResult(dados):
    d1 = float(dados[1])
    d2 = float(dados[2])
    controle = int(dados[0])

    if(controle == 1):
        return (d1+d2)
    elif(controle == 2):
        return (d1-d2)
    elif(controle == 3):
        return (d1*d2)
    elif(controle == 4):
        return (d1/d2)
    else: 
        return ("Operação inválida!")
      