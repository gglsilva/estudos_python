import random

class Jogador:

    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__vitorias = 0
        self.__jogada = ['pedra', 'papel', 'tesoura']

    def get_nome(self):
        return self.__nome

    def fazer_jogada(self):
        return random.choice(self.__jogada)

    def get_jogada(self):
        return self.__jogada

    def incremente_vitorias(self):
        self.__vitorias += 1

    def get_vitorias(self):
        return self.__vitorias