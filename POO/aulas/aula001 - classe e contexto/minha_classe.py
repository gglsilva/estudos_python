class MinhaClasse:

    def __init__(self, att):
        self.meu_atributo = 'Olá mundo!' # atributo da classe 
        self.meu_atributo2 = att
        
    # funções dentro do contexto de uma classe chamamos de metodos
    def meu_metodo(self):
        print('Entrou no metodo!')

    def meu_metodo2(self, num, mult):
        return num * mult

#objeto = MinhaClasse() # instancia da MinhaClasse
#objeto.meu_metodo()
#resultado = objeto.meu_metodo2(5, 3)
#print(resultado)
#print(objeto.meu_atributo)

# Definir um atribudo no momento em que o objeto é instanciado
objeto = MinhaClasse('Meu Atributo')
print(objeto.meu_atributo2)
