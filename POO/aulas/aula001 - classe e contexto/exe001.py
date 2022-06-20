class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal += 1')

    def voltar_canal(self):
        print('Canal -= 1')

    def escolher_canal(self, canal):
        print('Canal = {}'.format(canal))


controle_sala = ControleRemoto('samsung', 'sala')
print('TV: {}'.format(controle_sala.televisao))
print('Comodo: {}'.format(controle_sala.comodo))
controle_sala.avancar_canal()
controle_sala.voltar_canal()
controle_sala.escolher_canal(29)