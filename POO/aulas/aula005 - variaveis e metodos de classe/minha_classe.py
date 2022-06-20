"""
##### contexto da classe ##########
class MinhaClasse:

    estatico = 'lhama' # Variavel de classe ou estatica
    
    #quando declaramos uma variavel de estatica, uma copia dela é criada e compartilhada
    #a nivel de classe com todos os objetos(instancias) da classe, é essencialmente uma
    #variavel global
    

    def __init__(self, estado):
        self.estado = estado

####################################

### contexto do objeto ###
obj1 = MinhaClasse(True)
##########################
obj2 = MinhaClasse(False)

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
"""

#################################################
# maneira correta de declara uma variavel estatica
"""
variaveis estaticas(global) podem ser abstraidas como atribudos(estado)
dentro da classe, e ser manipulada no contexto da classe em si
"""

class MinhaClasse:

    estatico = 'lhama'

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        print(self.estatico)

    @classmethod        # decorador
    def mudar_estatico(cls):    # parecido com o self, so que ao inves de fazer referencia para a instancia, faz referencia para a classe em si
        cls.estatico = 'Programador'
    
obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.print_estatico()
obj1.mudar_estatico()
obj1.print_estatico()
    