class ViagemVeneza:
    def ida(self):
        print("Viagem de avião...")

    def dia1(self):
        print("Visita à Basílica de São Marcos na Praça São Marcos")

    def dia2(self):
        print("Visita ao Palácio Doge")

    def dia3(self):
        print("Aproveitar a comida próximo à Ponte Rialto")

    def retorno(self):
        print("Viagem de carro...")


class ViagemMalvinas:
    def ida(self):
        print("Viagem de ônibus...")

    def dia1(self):
        print("Apreciar a vida marinha de Banana Reef")

    def dia2(self):
        print("Praticar esportes aquáticos")

    def dia3(self):
        print("Relaxar na praia e aproveitar o sol")

    def retorno(self):
        print("Viagem de avião...")


def main():
    opcao = input("Qual local de viagem deseja fazer? [Veneza, Malvinas]: ")

    # Código repetido, toda vez que adicionar uma nova viagem,
    # tem que duplicar o IF com todas as chamadas de métodos.
    if opcao == "Veneza":
        viagem = ViagemVeneza()
        viagem.ida()
        viagem.dia1()
        viagem.dia2()
        viagem.dia3()
        viagem.retorno()
    elif opcao == "Malvinas":
        viagem = ViagemMalvinas()
        viagem.ida()
        viagem.dia1()
        viagem.dia2()
        viagem.dia3()
        viagem.retorno()
    else:
        print("Opção inválida")


main()
