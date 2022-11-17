from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):

    def __init__(self, modelo= None, cor= None, valor= None):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor

    def getInformacoes(self):
        return f'Modelo: {self.modelo}\nCor: {self.cor}\nPreço: {self.valor}'
        
    @abstractmethod
    def cadastrar():
        pass

#    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo= None, cor= None, valor= None, potenciaDaFonte= None):
        super().__init__(modelo, cor, valor)
        self._potenciaDaFonte = potenciaDaFonte
        print('DeskTop Construido')

    @property
    def potenciaDaFonte(self):
        return self._potenciaDaFonte

    @potenciaDaFonte.setter
    def potenciaDaFonte(self, valor):
        self._ = valor
    
    def getInformacoes(self):
        return super().getInformacoes() + f'\nPotencia da fonte: {self._potenciaDaFonte}'

    def cadastrar(self, modelo, cor, valor, potenciaDaFonte):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self._potenciaDaFonte = potenciaDaFonte

#    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# from Computador import Computador


class NotBook(Computador):
    def __init__(self, modelo=None, cor=None, valor=None, tempoDeBateria=None):
        super().__init__(modelo, cor, valor)
        self.__tempoDeBateria = tempoDeBateria
        print('NotBook Construido')

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, valor):
        self.__ = valor

    def getInformacoes(self):
        return super().getInformacoes() + f'\nTempo de bateria: {self.__tempoDeBateria} horas'

    def cadastrar(self, modelo, cor, valor, tempoDeBateria):
        self.modelo = modelo
        self.cor = cor
        self.valor = valor
        self.__tempoDeBateria = tempoDeBateria

#    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# from DeskTop import Desktop
# from NotBook import NotBook

d1 = Desktop()
d1.cadastrar("Asus", "Azul", 3500, 500 )
print(d1.getInformacoes())
print('---------------------')

n1 = NotBook()
n1.cadastrar("Sansung", "Preto", 5000, 5)
print(n1.getInformacoes())
print('---------------------')