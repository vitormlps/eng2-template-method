from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):
    def __init__(self, nome = None, tensao = None, preco = None, rotacoes = None):
        super().__init__(nome, tensao, preco)
        self.__rotacoes = rotacoes

    def get_nome(self):
        return self.nome
    def get_tensao(self):
        return self.tensao
    def get_preco(self):
        return self.preco
    def get_rotacoes(self):
        return self.__rotacoes

    def login(self, valor, nome, preco, tensao, rotacoes):
        if valor == 'admin':
            self.nome = nome
            self.preco = preco
            self.tensao = tensao
            self.__rotacoes = rotacoes
        else:
            pass

    def getInformacoes(self):
        return f'__Lixadeira__\nNome: {self.nome}\nTensão: {self.tensao}\nPreço: R$ {self.preco}\nRotações: {self.__rotacoes}'

    def cadastrar(self):
        self.nome = input('\nBem vindo ao cadastro de Lixadeiras!\nPrimeiramente, digite o NOME da Lixadeira: ')
        self.preco = input('\nAgora, digite o PREÇO da Lixadeira: ')
        self.tensao = input('\nDigite a TENSÃO: ')
        self.__rotacoes = input('\nAs ROTAÇÕES: ')
        print('\n__Lixadeira cadastrada com sucesso!__')
