# Importar modulos
from palavras import palavras
import random

# Seleciona a palavra

def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()


# Iniciar o jogo
def jogar(palavra):
    # Definir algumas variaveis
    palavra_a_completar = "_" * len(palavra)
    advinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

    # Boas vindas ao jogador
    print("Vamos jogar!")
    print(exibir_forca(tentativas))
    print("Esta é a palavra: %s" % palavra_a_completar)

    # Enquanto o usuario nao adivinhar e ainda houver tentativas
    while not advinhou and tentativas > 0:
        tentativa = input("Digite uma palavra ou letra para continuar: ").upper()

    # Tentativa de letra unica
    # Verifica se a tentativa é uma letra unica
        if len(tentativa) == 1 and tentativa.isalpha():
            # verfica se a letra ja foi utilizada
            if tentativa in letras_utilizadas:
                print("Voce ja utilizou essa letra antes: %s " % tentativa)
            # Verifica se a tentativa nao esta na palavra
            elif tentativa not in palavra:
                print("A letra %s não esta na palavra" % tentativa)
                tentativas -= 1
                letras_utilizadas.append(tentativa)
            # Quando a letra esta na palavra
            else:
                print("Voce acertou! a letra %s esta na palavra" % tentativa)
                letras_utilizadas.append(tentativa)
                # Transformar a palavra em uma lista
                palavra_lista = list(palavra_a_completar)

                #Onde pode substituir o undeline baseado na letra que foi passado
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indices:
                    palavra_lista[indice] = tentativa

                palavra_a_completar = "".join(palavra_lista)
                if "_" not in palavra_a_completar:
                    advinhou = True
        # TENTATIVA DE PALAVRA COMPLETA
        # Quando o usuário tenta advinhar a palavra toda da forca
        elif len(tentativa) == len(palavra) and tentativa.isalpha():

        # Palavra já utiliza
            if tentativa in palavras_utilizadas:
                print("Você já utilizou está palavra %s" % tentativa)
            # Palavra está errada
            elif tentativa != palavra:
                print("A palavra %s está incorreta!" % tentativa)
                tentativas -= 1
                palavras_utilizadas.append(tentativa)
            # Acertou a palavra
            else:
                advinhou = True
                palavra_a_completar = palavra



        # Tentativa invalida
        else:
            print("Tentativa invalida, tente novamente")

        # Exibir status do jogo
        print(exibir_forca(tentativas))
        print(palavra_a_completar)


    # Finaliza o jogo se o usuario adivinhou a palavra ou acabaram as tentativas:
    if advinhou:
        print("Parabens! Voce acertou a palavra")
    else:
        print("Acabaram as tentativas, a palavra era: %s" % palavra)

# Status do jogo
def exibir_forca(tentativas):
    estagios = [  # Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     /
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |
                  |
                  |
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |
                  |
                  |
                  |
                  -
              """
    ]

    return estagios[tentativas]

# Iniciacao do jogo e continuar jogando
def iniciar():
  palavra = selecionar_palavra()
  jogar(palavra)
  # Quando acaba o jogo, verfica se o usuario quer continuar jogando
  while input("Jogar novamente? (S/N)").upper() == "S":
    palavra = selecionar_palavra()
    jogar(palavra)

iniciar()