from retangulo import Retangulo
'''
b = int(input("Digite a base: "))
a = int(input("Digite a altura: "))

r1 =  Retangulo(b, a)
print(f'base e altura respectivamente: {r1.retorna_valor_lados()}')
print(f'area: {r1.calcula_area()}')
print(f'perimetro: {r1.calcular_perimetro()}')
'''
print('='*30)
print('{:^30}'.format('Medidas do local'))
print('='*30)
labo_area = int(input('Digite o lado 1 do local: '))
labo_altura = int(input('Digite o lado 2 do local: '))

r1 = Retangulo(labo_area, labo_altura)
print(f'voce precisará de {r1.calcula_area()}m de piso')
print(f'voce precisará de {r1.calcular_perimetro()}m de rodapé')