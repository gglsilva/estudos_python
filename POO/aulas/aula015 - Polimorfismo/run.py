from numpy import insert
from models import Insersor, Repositorio

class RepositorioFake(Repositorio):

    def __init__(self) -> None:
        super().__init__()

    def select(self, nome: str) -> None:
        return None

repo = RepositorioFake()
insersor = insert(repo)

data = insersor.inserir_dado('Lhama', 28)
print(data)