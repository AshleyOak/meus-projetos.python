# Começo do Jogo

import random

# Definir as variáveis

palavras = ['linguagem','programacao','computador','python','desenvolvedor','analista','desenvolvimento','algoritmo','matematica','ciencia','tecnologia','sistema','inteligencia','informatica','comunicacao','dados','calculo','software','hardware','rede','internet','processamento','fisica','biologia','estatistica','engenharia','programador','automacao','matriz','numeros','controle','algoritmos','digital']

# Escolhendo a palavra
palavra_secreta = random.choice(palavras)

digitadas = []
acertos = []
erros = 0

# Printando a quantidade de letras
print("Bem vindo ao jogo da Forca!\n")

print("A palavra tem", len(palavra_secreta), "letras.")

# Laço de repetição
while True:
    senha = ""
    for letra in palavra_secreta:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra_secreta:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra_secreta:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " \|  "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /  "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print("A palavra era: ", palavra_secreta)
        break