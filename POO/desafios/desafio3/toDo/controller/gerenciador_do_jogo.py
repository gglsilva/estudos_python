from model import Jogador

class GerenciadorDeJogo:

    def __init__(self) -> None:
        self.jogador1 = Jogador('juninho')
        self.jogador2 = Jogador('pedrinho')
    
    def jogar(self):
        jogador1_jogada = self.jogador1.fazer_jogada()
        print(f'Jogador 1 {jogador1_jogada}')
        jogador2_jogada = self.jogador2.fazer_jogada()
        print(f'Jogador 2 {jogador2_jogada}')

        resultado = self.__verificar_vencedor(jogador1_jogada, jogador2_jogada)
        print(resultado)

        if resultado == 1: self.jogador1.incremente_vitorias()
        elif resultado == 2: self.jogador2.incremente_vitorias()

        return self.mostrar_vitorias()

    def __verificar_vencedor(self, jogador1_jogada, jogador2_jogada):
        if jogador1_jogada == jogador2_jogada: return 0
        if (
            (jogador1_jogada == 'pedra' and jogador2_jogada == 'tesoura')
            or (jogador1_jogada == 'papel' and jogador2_jogada == 'pedra')
            or (jogador1_jogada == 'tesoura' and jogador2_jogada == 'papel')
            ): return 1
        else: return 2

    def mostrar_vitorias(self):
        return f'{self.jogador1.get_nome()} venceu {self.jogador1.get_vitorias()}, e {self.jogador2.get_nome()} venceu {self.jogador2.get_vitorias()}'
