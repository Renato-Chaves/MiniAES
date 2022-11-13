import random
blocks = [[["" for i in range(4)] for j in range(4)] for k in range(8)]
blockPass = [[["" for i in range(4)] for j in range(4)] for k in range(8)]
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%¨&*()_+"

# Função para critografar entrada do usuario
def criptografar(userInput, blocks, blockPass):
    x = 0
    for i in range(8):
        for j in range(4):
            for k in range(4):
                if x > len(userInput) - 1:
                    break
                blocks[i][k][j] = userInput[x]
                x = x + 1
    x = 0
    y = 0
    z = 0
    for i in range(8):
        for j in range(4):
            for k in range(4):
                if k%2==0:
                    blockPass[z][y][x] = blocks[i][j][k]
                    if blocks[i][j][k] != "":
                        blocks[i][j][k] = characters[random.randint(0,73)]
                    x = x + 1
                    if x >= 4:
                        x = 0
                        y = y + 1
                    if y >= 4:
                        y = 0
                        z = z + 1
    print("Chave do Conteudo: ")
    outputText = ""
    for i in range(8):
        for j in range(4):
            for k in range(4):
                outputText = outputText+blockPass[i][k][j]
    print(outputText)
    print("-------------")
    print("Conteudo Criptografado: ")
    outputText = ""
    for i in range(8):
        for j in range(4):
            for k in range(4):
                outputText = outputText+blocks[i][k][j]
    print(outputText)
    print("-------------")

# função para descriptografar texto previamente criptografado
def descriptografar(userInput, blocks, blockPass):
    x = 0
    y = 0
    z = 0
    for i in range(8):
        for j in range(4):
            for k in range(4):
                if k%2==0:
                    blocks[i][j][k] = blockPass[z][y][x]
                    x = x + 1
                    if x >= 4:
                        x = 0
                        y = y + 1
                    if y >= 4:
                        y = 0
                        z = z + 1
    print("Conteudo Descriptografado: ")
    outputText = ""
    for i in range(8):
        for j in range(4):
            for k in range(4):
                outputText = outputText+blocks[i][k][j]
    print(outputText)
    print("-------------")

# Função para limpar o conteudo criptografado
def clearArray(array):

    for i in range(len(array)):
        for j in range(len(array[0])):
            for k in range(len(array[0][0])):
                array[i][j][k] = ""

# Escolha de função pelo usuário
userInput = ""
userChoice = "1"
while(userChoice != "0"):
    print("===============")
    userChoice = input("Escolha a função que deseja executar:\n1- Criptografar um texto\n2- Descriptografar\n0- Finalizar programa\n>>> ")
    if userChoice == "1":
        clearArray(blocks)
        clearArray(blockPass)
        userInput = ""
        while(userInput == ""):
            userInput = input("Digite o texto que deseja criptografar: ")
        print("-------------")
        criptografar(userInput, blocks, blockPass)
    elif userChoice == "2":
        if userInput == "":
            print("Impossivel descriptografar um texto inexistente")
        else:
            descriptografar(userInput, blocks, blockPass)
