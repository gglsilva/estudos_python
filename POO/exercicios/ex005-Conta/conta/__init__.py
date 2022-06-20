class Conta(object):
    def __init__(self, numero, correntista, saldo=0):
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    
    def alterar_nome_correntista(self, nome):
        self.correntista = nome
        return self.correntista

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            return 'Saldo insuficiente'

    def __str__(self):
        return 'Conta: {}\nCorrentista: {}\nSaldo: {}'.format(self.numero, self.correntista, self.saldo)
    
