class Pessoa:   # Substantivo
    # usando type annotetions: tipagem a nivel de comentario
    def __init__(self, name: str, idade: int) -> None:
        self.name = name    # Substantivo
        self.idade = idade  # Substantivo

    def dirigir(self, veiculo: str) -> None: # verbo
        print('Dirigir um(a)'.format(veiculo))

    def cantar(self) -> None: # verbo
        print('LaLaLaLa')

    def apresentar_idade(self) -> int: # verbo
        return self.idade
    
