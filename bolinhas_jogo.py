import random

menu = {"azul":0, "verde":0, "laranja":0, "vermelho":0, "amarelo":0}
total_por_cor = 10

def escolha_jogo():
    jogo_escolhe = str(input("Digite qual jogo você quer: [1] Arte da Fuga ou [2] Último Sobrevivente: "))
    print(jogo_escolhe)
    while (jogo_escolhe not in ['1','2']):
        print("Não localizei seu jogo.")
        jogo_escolhe = str(input("Digite qual jogo você quer: [1] Arte da Fuga ou [2] Último Sobrevivente: "))
    return jogo_escolhe

def escolha_cor():
    cor_escolhe = str(input("Digite sua cor entre azul, verde, laranja, vermelho e amarelo:")).lower()
    while (cor_escolhe not in menu.keys()):
        print("Não localizei sua cor.")
        cor_escolhe = str(input("Digite sua cor entre azul, verde, laranja, vermelho e amarelo:")).lower()
    return cor_escolhe

def createList(n):
    lista = []
    for i in range(n + 1):
        lista.append(i)
    lista.remove(0)
    return lista

def sortear(lista):
    return random.choice(lista)

def valida_cor(numero):
    if numero>=1 and numero<=10:
        return 'azul'
    elif numero>=11 and numero<=20:
        return 'amarelo'
    elif numero>=21 and numero<=30:
        return 'laranja'
    elif numero>=31 and numero<=40:
        return 'vermelho'
    elif numero>=41 and numero<=50:
        return 'verde'

def valida_jogo(jogo_escolhe, cor_escolhe):
    if jogo_escolhe == '1':
        return arte_da_fuga(cor_escolhe)
    elif jogo_escolhe == '2':
        print(ultimo_sobrevivente(cor_escolhe))

def arte_da_fuga(cor_escolhe):
    lista = createList(50)
    tentativas = 0
    while True:
        sorteado = sortear(lista)
        lista.remove(sorteado)
        tentativas +=1
        cor = valida_cor(sorteado)
        if cor == cor_escolhe:
            print('Você tirou {} bolinha(s) da cor {} em {} tentativa(s)!'.format(sorteado, cor, tentativas))
            break
    return tentativas

def ultimo_sobrevivente(cor_escolhe):
    lista = createList(50)
    tentativas = 0
    while True:
        sorteado = sortear(lista)
        lista.remove(sorteado)
        cor = valida_cor(sorteado)
        menu[cor] += 1
        tentativas += 1

        resultado = regra(menu)
        if (resultado):
            if cor_escolhe in resultado.keys():
                return 'Você é o último sobrevivente, sobreviveu a {} tentativa(s) da sua cor {} com {} bolinha(s)!'.format(tentativas, cor_escolhe, resultado[cor_escolhe])
            else:
                return 'Não sobreviveu!'

def regra(menu):
    soma = 0
    novo_menu = menu.copy()

    for cor in menu.keys():
        if (menu[cor] == 10):
            soma += 10
            novo_menu.pop(cor)
    if soma >= 40:
        return novo_menu
    else:
        return None

jogo_escolhe = escolha_jogo()
cor_escolhe = escolha_cor()
valida_jogo(jogo_escolhe, cor_escolhe)
