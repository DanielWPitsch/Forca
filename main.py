#jogo da forca

import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    # Método Construtor
    def __init__(self, word):
        self.word=word
        print("construtor criado com sucesso!")
    # Método para adivinhar a letra
    def guess(self, palavra, letra):
        if letra in palavra:
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self, acertos, tamanho):
        if acertos == tamanho:
            return True
        else:
            return False

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self, erros, tamanho):
        print(board[erros])
    def getWord(self):
        return self.word

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())
    #string
    palavra = game.getWord()
    tamanho = len(game.getWord())
    palpites = ["*"]*tamanho
    acertos = erros = 0
    todas=[]

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    while(acertos<tamanho and erros<6):
        # Verifica o status do jogo
        game.print_game_status(erros, tamanho)
        letra=input("Qual letra você acha que tem na palavra?")
        while(letra in todas):
            print("tentativa repetida, por favor digite uma letra diferente")
            letra = input("Qual letra você acha que tem na palavra?")
        todas.append(letra)
        for i in range(tamanho):
            if (letra == palavra[i]):
                palpites[i] = letra
                acertos += 1
            print(palpites[i], end="")
        if(game.guess(palavra, letra)):
            print("\nAcertou!")
        else:
            erros+=1
            print("\nErrou!")

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won(acertos, tamanho):
        print('\nParabéns! Você venceu!!')
    else:
        game.print_game_status(erros, tamanho)
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()

