from components.elevador import Elevador

elevador = Elevador()

while (True):
    andar = int(input('Defina um andar: '))
    if andar == 0 or andar > elevador.andarMaximo or andar < elevador.andarMinimo:
        print('Andar inválido!')
    elif andar == 999:
        print('Saindo do elevador...')
        break
    else:
        elevador.transitar_andar(andar)
    
