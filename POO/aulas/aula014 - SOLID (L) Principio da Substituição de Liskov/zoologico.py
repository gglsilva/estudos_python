from typing import Type
# O principio de liscove resumidamente diz que sempre que tivemos a ideia de Herança entre classes,
# devemos fazer o elemento mais generico no topo da hierarquia e aparti disso ir expecificando conforme 
# desemos na arvore de objetos.

# classe Mãe
class Animal:

    def comer(self) -> None:
        print('O Animal Esta comendo')

    def andar(self) -> None:
        print('O Animal Esta andando')

    def dormir(self) -> None:
        print('O Animal Esta dormindo')


# classe filha subtipo da classe Mãe Animal
class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self) -> None:
        print('Aves Esta cantando')


class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()


    def escorregar(self) -> None:
        print('Pinguim Esta escorregando no gelo')


class Lobos(Animal):

    def __init__(self) -> None:
        super().__init__()

    def uivar(self) -> None:
        print('Lobos Esta uivando')


class Pessoa:

    def observar(self, animal: Type[Animal]) -> None:
        animal.comer()
