## Template Method | Engenharia de Software 2 
Trabalho acadêmico sobre o padrão de design de software Template Method.

### Contribuidores
<a href="github.com/Plankito"><img src="https://github.com/Plankito.png" width="45" height="45"></a> &nbsp;
<a href="github.com/SAULvaRGAS88"><img src="https://github.com/SAULvaRGAS88.png" width="45" height="45"></a> &nbsp;
<a href="github.com/vitormlps"><img src="https://github.com/vitormlps.png" width="45" height="45"></a> &nbsp;

### Descrição
Apresentando o template method ou Método Modelo, é sugerida a definição de um esqueleto para algoritmos em suas determinadas operações, permitindo que o algoritmo definido seja sujeito à mudanças através das subclasses, onde preza-se pela conservação da estrutura padrão do algoritmo, o esqueleto.
Frameworks fazem uso extensivo do padrão Template Method. Qualquer framework executa os componentes imutáveis de um domínio assim como cria placeholders para qualquer escolha relevante de modificação pelo usuário.

#### Aplicação
O Template Method permite que você transforme um algoritmo monolítico (uma coisa só. algo grande) em uma série de etapas individuais (particiona o algoritmo) que podem facilmente ser estendidas por subclasses enquanto ainda mantém intacta a estrutura definida em uma superclasse.
Aplica-se o Template Method, quando você precisa de variações de um mesmo algoritmo sem mudar a ordem de execução dos métodos.

#### Exemplo (em Python)
```
from abc import ABCMeta, abstractmethod

class ClasseAbstrata(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operacao1(self):
        pass

    @abstractmethod
    def operacao2(self):
        pass

    def template_method(self):
        print("Definindo o algoritmo: Operação 1 após Operação 2")
        self.operacao2()
        self.operacao1()

class ClasseConcreta(ClasseAbstrata):
    def operacao1(self):
        print("Minha operação concreta 1")

    def operacao2(self):
        print("Minha operação concreta 2")

class Cliente:
    def main(self):
        self.concreta = ClasseConcreta()
        self.concreta.template_method()

cliente = Cliente()
cliente.main()
```

### Desenvolvimento do padrão em um código sem o padrão

Pasta:`[./padrao-aplicado/](https://github.com/vitormlps/eng2-template-method/tree/main/padrao-aplicado)`

`[./padrao-aplicado/codigo-base.py](https://github.com/vitormlps/eng2-template-method/tree/main/padrao-aplicado/codigo-base.py)` → Representação de itinerários de viagem de uma agência de turismo, sendo cada viagem uma classe. A duplicação de código pode ser vista na lógica de consumo dessas classes ao implementar o itinerário.

`[./padrao-aplicado/padrao-aplicado.py](https://github.com/vitormlps/eng2-template-method/tree/main/padrao-aplicado/padrao-aplicado.py)` → Com o método template aplicado, a lógica de consumo fica mais simples de desenvolver e fácil para outros desenvolvedores entenderem. Ainda é possível desenvolver lógica dinâmicamente, deixando o código mais fácil para realizar manutenção.

### Identificação do padrão em APIs de linguagens de programação
Todos os métodos não abstratos do java.io.InputStream, java.io.OutputStream, java.io.Reader, java.io.Writer, java.util.AbstractList, java.util.AbstractSet e java.util.AbstractMap utilizam o padrão.

Também, na classe javax.servlet.http.HttpServlet, todos os métodos “doXXX()” enviam o HTTP 405 erro “Method Not Allowed” por padrão. 

Outras funcionalidades de APIs e frameworks que utilizam o padrão:
- Método onMessage do MDB's
- Classe Struts Action
- Classes de data access do Spring
- ASP.NET page life cycle
- Geradores de códigos
- XML parser
- Validação em componentes de negócio
- Utilidade customizável de logging

### Identificação de refatoração de projetos antigos do grupo

Pasta: `[./projetos-antigos/](https://github.com/vitormlps/eng2-template-method/tree/main/projetos-antigos)`

`[./orientacao-a-objetos-informativo-covid/](https://github.com/vitormlps/eng2-template-method/tree/main/projetos-antigos/orientacao-a-objetos-informativo-covid)` → O padrão pode ser aplicado nas funções de verificação, pois existem de string, se digitou ‘não’, se está duplicado, se é número e de relação. O aplicar permitirá que o código duplicado seja reduzido através do agrupamento das verificações em uma única classe.

### Vantagens e desvantagens
#### Pontos fortes
- Fit natural para construir frameworks.
- Uma das principais vantagens é que não há duplicação de código.
- Há reutilização de código uma vez que o padrão utiliza herança e não composição.
- A flexibilidade permite que as subclasses decidam como implementar os passos do algoritmo.
- É possível deixar clientes sobrescrever apenas certas partes de um algoritmo grande, tornando-os menos afetados por mudanças que ocorrem por outras partes do algoritmo.
- Possibilidade de elevar o código duplicado para uma superclasse.

#### Pontos fracos
- Debugar a aplicação e compreender a sequência do fluxo no padrão pode ser confuso. 
- Possibilidade de implementar um método que não deveria ser implementado ou deixar de implementar um método abstrato.
- A manutenção dos componentes de alto ou baixo nível pode causar problemas na implementação.
- Alguns clientes podem ser limitados ao fornecer o esqueleto de um algoritmo.
- É possível violar o princípio de substituição de Liskov ao suprimir uma etapa padrão de implementação através da subclasse.
- Implementações do padrão tendem a ser mais difíceis de se manter quanto mais etapas eles tiverem.

### Conclusão
Fruto dos dados expostos é possível evidenciarmos certos benefícios do uso desse modelo, principalmente quando relacionado a otimização da codificação, onde a mesma é sujeita ao benefício do controle de redundâncias em métodos que o modelo implica.
Contudo, é clara a diversidade de funcionalidades de APIs e frameworks que utilizam o padrão, trazendo à tona a popularidade e eficácia da aplicação do mesmo, o que torna os códigos necessariamente mais enxutos.
