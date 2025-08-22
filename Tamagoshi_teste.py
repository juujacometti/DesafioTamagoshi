# Classe mãe 
class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0 
        self.saude = 100
        self.idade = 0
        self.tedio = 0

# COISAS FALTANTES 
# terminar de colocar a condição das outras raças sobre comida e brincadeiras (julya)
# definição das duas racas (yasme)
# o benefício das outras 2 raças (yasme)
# os desafios (julya e yasme) 
# definição de função de tempo, idade, saude e humor (julya e yasme)
# chamar todas as funções para funcionamento do jogo

    # Função que verifica as condições da brincadeira
    def brincar(self, escolhaBrincadeira):
        if (self.tedio >= 0) and (self.tedio <= 100):    # Verifica se o tamagoshi está com algum nível de tédio           
            # Condição que verifica se a raça escolhida pelo usuário é a de água. Apenas ela beneficia com as brincadeiras
            if isinstance(self, Agua):    
                if escolhaBrincadeira == 1:    # Brincadeira que envolve água diminui o tédio mais rápido
                    self.tedio -= 30
                elif escolhaBrincadeira in [2, 3, 4]:    # Brincadeiras 'favoritas' de outras raças
                    self.tedio -= 15
                elif escolhaBrincadeira == 5:    # Brincadeira genérica
                    self.tedio -= 10
                elif escolhaBrincadeira == 6:    # Cancelar escolha de brincadeiras
                    print("Brincadeira cancelada.")
        else:
            print(f"O(A) {self.nome} não está com tédio.") 
        return self.tedio
    
    # Função que verifica as condições de alimentação
    def alimentar(self, escolhaComida):
        if (self.fome >= 0) and (self.fome <= 100):
            # Condição que verifica se a raça escolhida pelo usuário é a de fogo. Apenas ela beneficia com a alimentaçãi
            if isinstance(self, Fogo):
                if escolhaComida in [1, 2, 3]:
                    self.fome -= 10
                elif escolhaComida == 4:
                    self.fome -= 25 
                elif escolhaComida == 

# Criação de raças
class Agua(Tamagoshi):
    def __init__(self, nome, cor):
        super().__init__(nome)    # Chamada do construtor da classe mãe
        self.cor = cor
        self.tedio = 15    # Definição de atributos específicos da raça
        self.tamanho = 2

class Fogo(Tamagoshi):
    def __init__(self, nome, cor):
        super().__init__(nome)    # Chamada do construtor da classe mãe
        self.cor = cor
        self.tedio = 15    # Definição de atributos específicos da raça
        self.fome = 15
        self.tamanho = 3


# Listas (brincadeiras, comida)
                    # Água            Terra               Ar                Fogo               
listaBrincadeiras = ["Ir na piscina", "Castelo de areia", "Soltar pipa", "Jogar queimada", "Video game", "Cancelar escolha"]
listaComidas = ["Gelatina", "Batata", "Pipoca", "Pimenta", "Sorvete"]




escolhaBrincadeiras = int(input(f"===== BRINCADEIRAS 😁 =====\nEscolha uma das brincadeiras a seguir:\n1 - 🏊‍♀️ {listaBrincadeiras[0]}\n2 - 🏰 {listaBrincadeiras[1]}\n3 - 🪁 {listaBrincadeiras[2]}\n4 - 🤾‍♀️ {listaBrincadeiras[3]}\n5 - 🎮 {listaBrincadeiras[4]}\n6 - ❌{listaBrincadeiras[5]}\n===============\nEscolha => "))
escolhaComida = int(input(f"===== COMIDAS 😋 =====\nEscolha uma das comidas a seguir:\n1 - 🍮 {listaComidas[0]}\n2 - 🥔 {listaComidas[1]}\n3 - 🍿 {listaComidas[2]}\n4 - 🌶 {listaComidas[3]}\n5 - 🍦 {listaComidas[4]}\n6 - ❌ {listaComidas[5]}\n===============\nEscolha => "))          