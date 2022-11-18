from Ferramenta import Ferramenta

class Furadeira(Ferramenta):
    def __init__(self, nome = None, preco = None, tensao = None, potencia = None):
        super().__init__(nome, preco, tensao)
        self._potencia = potencia

    def get_nome(self):
        return self.nome
    def get_tensao(self):
        return self.tensao
    def get_preco(self):
        return self.preco
    def get_potencia(self):
        return self._potencia

    def login(self, valor, nome, preco, tensao, potencia):
        if valor == 'admin':
            self.nome = nome
            self.preco = preco
            self.tensao = tensao
            self._potencia = potencia
        else:
            pass

    def getInformacoes(self):
        return f'__Furadeira__\nNome: {self.nome}\nTensão: {self.tensao}\nPreço: R$ {self.preco}\nPotência: {self._potencia}'

    def cadastrar(self):
        self.nome = input('\nBem vindo ao cadastro de Furadeiras!\nPrimeiramente, digite o NOME da Furadeira: ')
        self.preco = input('\nAgora, digite o PREÇO da Furadeira: ')
        self.tensao = input('\nDigite a TENSÃO: ')
        self._potencia = input('\nA POTÊNCIA: ')
        print('\n__Furadeira cadastrada com sucesso!__')
