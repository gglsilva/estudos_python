# classe aplicando o princípio de aberto/fechado
"""
fechada para auterações e aberta para exetensões
"""
class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')
        

class Palhaço:
    
    def apresentar_show(self):
        print('Palhaço apresentando seu show')

  
circo = Circo()
malabarista = Malabarista()
palhaço = Palhaço()

circo.apresentar(malabarista)
circo.apresentar(palhaço)

# Isso gera uma associação entre as classes, sempre que o metodo 'apresentar' da classe Circo for chamado
# passando passando a instancia de Malabarista ou Palhaço como parametro ele irar chamar o metodo apresentar_show
# da classe Malabarista ou Palhaço e assim sucessivamente se tivessemos outras classes que fossem associadas ao metodo
# a motivação do princípio aberto/fechado é que entradas diferentes geram ações diferentes