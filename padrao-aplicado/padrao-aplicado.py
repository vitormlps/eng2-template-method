from abc import ABCMeta, abstractmethod

# Em códigos pequenos, a desvantagem
# é adicionar uma classe extra, ...
class Viagem(metaclass=ABCMeta):
    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    # ... mas vale a pena, pois fica mais
    # fácil de dar manutenção ...

    # Método Template (Template Method)
    def itinerario(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()


class ViagemVeneza(Viagem):
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


class ViagemMalvinas(Viagem):
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


class AgenciaDeTurismoBasica:
    def preparar_viagem(self):
        opcao = input("Qual local de viagem deseja fazer? [Veneza, Malvinas]: ")

        # ... e na hora de construir
        # a lógica que consome o método template,
        # o código fica bem reduzido.
        if opcao == "Veneza":
            self.viagem = ViagemVeneza()
            self.viagem.itinerario()
        elif opcao == "Malvinas":
            self.viagem = ViagemMalvinas()
            self.viagem.itinerario()
        else:
            print("Opção inválida")


# Além de possibilitar a implementação de lógicas
# mais avançadas e dinâmicas:
class AgenciaDeTurismoAvancada:
    viagens = [ViagemVeneza, ViagemMalvinas]

    def preparar_viagem(self):
        opcao = input("Qual local de viagem deseja fazer? [Veneza, Malvinas]: ")
        found = False

        for viagem in self.viagens:
            if opcao in viagem.__name__:
                found = True
                viagem().itinerario()
                break
            else:
                found = False

        if not found:
            print("Opção inválida")


print("\nExemplo de lógica básica")
agenciaBasica = AgenciaDeTurismoBasica()
agenciaBasica.preparar_viagem()

print("\nExemplo de lógica avançada")
agenciaAvancada = AgenciaDeTurismoAvancada()
agenciaAvancada.preparar_viagem()
