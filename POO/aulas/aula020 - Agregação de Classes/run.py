from produtos import  Produto
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 5)

car.adicionar_produto(monitor)
car.adicionar_produto(cerveja)
car.adicionar_produto(cerveja)

car.finalizar_compra()
