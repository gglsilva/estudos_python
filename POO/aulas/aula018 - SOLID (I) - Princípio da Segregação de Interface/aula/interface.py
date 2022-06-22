from abc import ABC, abstractmethod
# na implementação de inferface não é necessario definir metodos privados
# pois eles não são visiveis ao usuario, e podem ser implementados diretamente na classe em si
'''
Antes
class Ave(ABC):

    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'
'''
#depois
class AveVoadora(ABC):
    
    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def voar(self):
        raise 'Should implement voar method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'

class AveQueNaoVoa(ABC):
    
    @abstractmethod
    def comer(self):
        raise 'Should implement comer method'

    @abstractmethod
    def gritar(self):
        raise 'Should implement gritar method'