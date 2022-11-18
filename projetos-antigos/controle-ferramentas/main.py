from Furadeira import Furadeira
from Lixadeira import Lixadeira

lLixadeira = []
lFuradeira = []

def cadastrarFuradeira():
  furadeira = Furadeira()
  furadeira.cadastrar()
  lFuradeira.append(furadeira)
  write_append_Furadeira()

def cadastrarLixadeira():
  lixadeira = Lixadeira()
  lixadeira.cadastrar()
  lLixadeira.append(lixadeira)
  write_append_Lixadeira()

def listarFuradeira():
  if lFuradeira == []:
    print('\n  __NENHUMA Furadeira cadastrada!__')
  else:
    for furadeira in lFuradeira:
      print(f'\n{furadeira.getInformacoes()}')

def listarLixadeira():
  if lLixadeira == []:
    print('\n  __NENHUMA Lixadeira cadastrada!__')
  else:
    for lixadeira in lLixadeira:
      print(f'\n{lixadeira.getInformacoes()}')

def write_append_Furadeira():
  arquivo = open('Furadeiras.txt', 'w')
  for Furadeira in lFuradeira:
    arquivo.write(f'{Furadeira.get_nome()};{Furadeira.get_preco()};{Furadeira.get_tensao()};{Furadeira.get_potencia()}\n')
  arquivo.close()

def write_append_Lixadeira():
  arquivo = open('Lixadeiras.txt', 'w')
  for Lixadeira in lLixadeira:
    arquivo.write(f'{Lixadeira.get_nome()};{Lixadeira.get_preco()};{Lixadeira.get_tensao()};{Lixadeira.get_rotacoes()}\n')
  arquivo.close()

def read():
  arquivo = open('Furadeiras.txt', 'r')
  for linha in arquivo:
    lista = linha.strip().split(';')
    furadeira = Furadeira()
    furadeira.login('admin', lista[0], lista[1], lista[2], lista[3])
    lFuradeira.append(furadeira)
  arquivo.close()

  arquivo = open('Lixadeiras.txt', 'r')
  for linha in arquivo:
    lista = linha.strip().split(';')
    lixadeira = Lixadeira()
    lixadeira.login('admin', lista[0], lista[1], lista[2], lista[3])
    lLixadeira.append(lixadeira)
  arquivo.close()

menuFuradeira = """ 
  ==================================================================
                             FURADEIRAS    
  ==================================================================
  0- Voltar ao MENU de Ferramentas
  1- Cadastrar Furadeira
  2- Listar Furadeiras
  ==================================================================
  --> Digite "EXIT" a qualquer momento para voltar ao menu.
  ==================================================================
  Escolha: """

menuLixadeira = """ 
  ==================================================================
                             LIXADEIRAS   
  ==================================================================
  0- Voltar ao MENU de Ferramentas
  1- Cadastrar Lixadeira
  2- Listar Lixadeiras
  ==================================================================
  --> Digite "EXIT" a qualquer momento para voltar ao menu.
  ==================================================================
  Escolha: """

menu = """ 
  ==================================================================
                                MENU    
  ==================================================================
  0- Finalizar o Programa
  1- Menu de Furadeiras
  2- Menu de Lixadeiras
  ==================================================================
  --> Digite "EXIT" a qualquer momento para voltar ao menu.
  ==================================================================
  Escolha: """

def MENUfuradeira():
  n_digit = input(menuFuradeira)

  if n_digit == '0': MENU()

  elif n_digit == '1': cadastrarFuradeira()
  elif n_digit == '2': listarFuradeira()

  else:
    input(' >>> ERRO.  Opção inválida.[ENTER]')
    MENU()

def MENUlixadeira():
  n_digit = input(menuLixadeira)

  if n_digit == '0': MENU()

  elif n_digit == '1': cadastrarLixadeira()
  elif n_digit == '2': listarLixadeira()

  else:
    input(' >>> ERRO.  Opção inválida.[ENTER]')
    MENU()

def MENU():
  n_digit = input(menu)

  if n_digit == '0': exit()

  elif n_digit == '1': MENUfuradeira()
  elif n_digit == '2': MENUlixadeira()

  else:
    input(' >>> ERRO.  Opção inválida.[ENTER]')
    MENU()
read()
while True:
    MENU()
