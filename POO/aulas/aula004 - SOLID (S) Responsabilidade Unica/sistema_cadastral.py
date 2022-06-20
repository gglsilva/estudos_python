class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print('Cadastrar o Usuario {}, Idade {}'.format(nome, idade))
        else:
            print('dados inválidos!')