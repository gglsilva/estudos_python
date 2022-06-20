class Error:

    @staticmethod
    def protocolo():
        print('Protocolo apresenta Erro')

    @staticmethod
    def entrada():
        print('Entrada apresenta Erro')

    @staticmethod
    def error_500():
        print('Internal Server Error')

    @staticmethod
    def error_404():
        print('Not Found Error')

Error.entrada()
# conseguimos fazer um agrupamento de erros sem ter um objeto atuando sobre eles
# os @staticmethod podem ser usados como coleções de contextos que não estão 
# exatamente ligados entre si