class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    def brincar(self, quantidade, escolhaBrincadeira):
        if (quantidade >= 0) and (quantidade <= 100):           
            if isinstance(self, Agua):
                if escolhaBrincadeira == 1:
                    self.tedio -= 30
                elif escolhaBrincadeira in [2, 3, 4]:
                    self.tedio -= 15
                elif escolhaBrincadeira == 5:
                    self.tedio -= 10
                elif escolhaBrincadeira == 6:
                    print("Brincadeira cancelada.")
            else:
                self.tedio -= 10
        else:
            print(f"O(A) {self.nome} não está com tédio.")
        

    


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


            
                    # Água            Terra               Ar                Fogo               
listaBrincadeiras = ["Ir na piscina", "Castelo de areia", "Soltar pipa", "Jogar queimada", "Pular corda", "Cancelar escolha"]
escolhaBrincadeiras = int(input(f"===== BRINCADEIRAS 😁 =====\nEscolha uma das brincadeiras a seguir:\n1 - 🏊‍♀️ {listaBrincadeiras[0]}\n2 - 🏰 {listaBrincadeiras[1]}\n3 - 🪁 {listaBrincadeiras[2]}\n4 - {listaBrincadeiras[3]}\n5 - {listaBrincadeiras[4]}\n6 - {listaBrincadeiras[5]}\nEscolha => "))          
    