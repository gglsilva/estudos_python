from models import Elevador
from controller import GerenciadorDeElevador

controllerElevador = GerenciadorDeElevador(Elevador(1), Elevador(2))

while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))
    resposta = controllerElevador.transitar(elevadorId, andar)
    print(resposta)
