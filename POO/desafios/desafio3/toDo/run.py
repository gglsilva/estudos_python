from controller import GerenciadorDeJogo

ctrl = GerenciadorDeJogo()

while (True):
    input()
    result = ctrl.jogar()
    print(result)
    print()
