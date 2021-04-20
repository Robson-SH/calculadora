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
    dados[1] = float(dados[1])
    dados[2] = float(dados[2])
    dados[0] = int(dados[0])

    if(dados[0] == 1):
        return (dados[1]+dados[2])
    elif(dados[0] == 2):
        return (dados[1]+dados[2])
    elif(dados[0] == 3):
        return (dados[1]+dados[2])
    elif(dados[0] == 4):
        return (dados[1]+dados[2])
    else: 
        return ("Operação inválida!")
      