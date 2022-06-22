from terrenos.quadrado import TerrenoQuadrado   
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Geraldo')
TerrenoQuadrado = TerrenoQuadrado(4)
TerrenoRetangular = TerrenoRetangular(2, 3)

engenheiro.medir_area(TerrenoQuadrado)
engenheiro.medir_area(TerrenoRetangular)

engenheiro.medir_perimetro(TerrenoRetangular)