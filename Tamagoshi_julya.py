# COISAS FALTANTES 
# definição das duas racas (yasme)
# o benefício das outras 2 raças (yasme)
# os desafios (função dormir realizada, falta a de acordar e linkar elas) (julya e yasme) 
# definição de função de vida, tempo (yasme)
# chamar todas as funções para funcionamento do jogo e incluir coisas que você alterar


# ====== Classe mãe ======
class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0 
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.dormindo = False
        
    def statusPet(self):
        print(f"\n{25 * '='}\nSTATUS DE {self.nome}")
        print(f"😋 Fome: {self.fome}")
        print(f"😷 Saúde: {self.saude}")
        print(f"🙄 Tédio: {self.tedio}")
        print(f"🤔 Humor: {self.humor()}")
        print(f"📏 Idade: {self.idade}")
        if isinstance(self, Aquati):
            print(f"💧 Hidratação: {self.hidratacao}")
        elif isinstance(self, Fuegui):
            print(f"Calor: {self.calor}")
            
            
    def acoes(self):
        listaAcao = [f"1 - 🥗 Alimentar", "2 - 🕹️ Brincar", "3- ⏳ Passar o tempo", "Necessidade da raça", "5 - ❌ Sair (o pet irá dormir)"]
        
        if isinstance(self, Aquati):
            listaAcao[3] = "4 - 💧 Hidratar"
        elif isinstance(self, Fuegui):
            listaAcao[3] = "4 - 🔥 Esquentar"
        
        
        print(listaAcao)
        


    # Verifica as condições da brincadeira
    def brincar(self, escolhaBrincadeira):
        if (self.tedio >= 0) and (self.tedio <= 100):    # Verifica o nível de tédio           
            if isinstance(self, Aquati):    # Condição que verifica se a raça escolhida pelo usuário é a de água. Apenas ela beneficia com as brincadeiras.
                if escolhaBrincadeira == 1:    # Brincadeira que envolve água diminui o tédio mais rápido
                    self.tedio = max(0, self.tedio - 30)    # Garante que o valor não seja negativo, caso fique, será substituído para zero
                    print(f"{self.nome} fez sua brincadeira favorita! 🤩")
                elif escolhaBrincadeira in [2, 3, 4]:    # Brincadeiras 'favoritas' de outras raças
                    self.tedio = max(0, self.tedio - 15)
                elif escolhaBrincadeira == 5:    # Brincadeira genérica
                    self.tedio = max(0, self.tedio - 10)
                elif escolhaBrincadeira == 6:    # Cancelar escolha de brincadeiras
                    print("Brincadeira cancelada.")
            else:    # Outras raças
                if escolhaBrincadeira in [1, 2, 3, 4]:
                    self.tedio = max(0, self.tedio - 15)
                elif escolhaBrincadeira == 5:
                    self.tedio = max(0, self.tedio - 10)
                elif escolhaBrincadeira == 6:
                    print("Brincadeira cancelada")
        else:
            print(f"{self.nome} não está com tédio.") 
        print(f"Nível de tédio: {self.fome}")    # Informação para o usuário

    
    # Verifica as condições de alimentação
    def alimentar(self, escolhaComida):
        if (self.fome >= 0) and (self.fome <= 100):    # Verifica o nível de fome
            if isinstance(self, Fuegui):     # Condição que verifica se a raça escolhida pelo usuário é a de fogo. Apenas ela beneficia com a alimentação.
                if escolhaComida in [1, 2, 3]:
                    self.fome = max(0, self.fome - 15)
                elif escolhaComida == 4:
                    self.fome = max(0, self.fome - 25)
                    print(f"{self.nome} comeu sua comida favorita! 🤩")
                elif escolhaComida == 5:
                    self.fome = max(0, self.fome - 10)
                elif escolhaComida == 6:
                    print("Alimentação cancelada.")
            else:    # Outras raças 
                if escolhaComida in [1, 2, 3, 4]:
                    self.fome = max(0, self.fome - 15)
                elif escolhaComida == 5:
                    self.fome = max(0, self.fome - 10)
                elif escolhaComida == 6:
                    print("Alimentação cancelada")
        else:
            print(f"{self.nome} não está com fome!")
        print(f"Nível de fome: {self.fome}")    # Informação para o usuário
    
    
    # Verifica o humor
    def humor(self):
        humor = 100 - ((self.fome + self.tedio) / 2)
        # Condição que define o humor 
        if humor <= 25:
            print("Humor: Triste 😭")
        elif humor <= 50:
            print("Humor: Estável 😐")
        elif humor <= 75:
            print("Humor: Bem ☺️")
        else:
            print("Humor: Muito feliz! 😁")
            
            
    # Verifica se está dormindo         
    def dormir(self):
        self.dormindo = True
        print(f"{self.nome} está dormindo agora... 😴")
        
    def acordar(self):
        self.dormindo = False
        print(f"{self.nome} está acordado! 🌞")
        
    
    # Verifica a vida (ESTÁ IGUAL AO DA MARI, NÃO MEXI)
    # Diminui a saúde do bichinho conforme as condições de fome (quanto mais alta, pior)
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 60)) or ((self.tedio > 60 and self.tedio <= 60)):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 60)):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print("Estou morrendo.......AHHHHHH 💀")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu ⚰️")
            
    
    # Verifica o passar do tempo (ESTÁ IGUAL AO DA MARI, NÃO MEXI)
    def tempoPassando(self):
        self.vida() # Atualiza a saúde baseado na sua fome e tédio atuais
        self.idade += 0.2 # O tempo passa e o pet envelhece
        self.tedio += 2.5 # Aumenta o tédio com o passar do tempo
        self.fome -= 5


# ====== Criação de raças ======
#Raça de água
class Aquati(Tamagoshi): 
    def __init__(self, nome):
        super().__init__(nome)    # Chamada do construtor da classe mãe  
        self.hidratacao = 100    # Definição de atributos específicos da raça
        
    # Necessidade específica da raça
    def hidratar(self):
        self.hidratacao += 25
        print(f" {self.nome} bebeu água! 💧")
        
        
# Raça de fogo
class Fuegui(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)    # Chamada do construtor da classe mãe
        self.calor = 100    # Definição de atributos específicos da raça
        
     # Necessidade específica da raça
    def esquentar(self):
        self.calor += 25
        print(f"{self.nome} se esquentou e se sente melhor! ♨️")
        
        
# Raça de ar
# Da um nome diferentinho pras raças 

# Raça de terra

        
# ====== Funcionamento do jogo ======
def main():
    # Interações iniciais
    print(f"{25 * '='}\n  🌱🌬️  PET VIRTUAL 💧🔥 \n")
    nome = input("=> Informe o nome do seu novo pet: ")
    
    escolhaRaca = int(input(f"=> Escolha a raça de {nome}:\n\n1 - Aquati (Água 💧)\n  * Possui vantagem com as brincadeiras\n  * Necessidade especial: Hidratação\n\n2 - Fuegui (Fogo 🔥)\n  * Possui vantagem com a alimentação\n  * Necessidade especial: Calor\n\n3 - \n\n4 -\n\nInforme sua escolha (1, 2, 3 ou 4): "))
    # Condição para raça específica
    if escolhaRaca == 1:
        pet = Aquati(nome)
    elif escolhaRaca == 2:
        pet = Fuegui(nome)

    
    # Looping principal do jogo
    while True:
        
        pet.statusPet()
        pet.acoes()
        
        
        
        escolhaAcao = int(input("x "))

    




main()






# Retirar daqui
# Listas (ação, brincadeiras, comida)
                    # Água            Terra               Ar                Fogo               
listaBrincadeiras = ["Ir na piscina", "Castelo de areia", "Soltar pipa", "Jogar queimada", "Video game", "Cancelar escolha"]
listaComidas = ["Gelatina", "Batata", "Pipoca", "Pimenta", "Sorvete", "Cancelar alimentação"]






escolhaBrincadeiras = int(input(f"===== BRINCADEIRAS 😁 =====\nEscolha uma das brincadeiras a seguir:\n1 - 🏊‍♀️ {listaBrincadeiras[0]}\n2 - 🏰 {listaBrincadeiras[1]}\n3 - 🪁 {listaBrincadeiras[2]}\n4 - 🤾‍♀️ {listaBrincadeiras[3]}\n5 - 🎮 {listaBrincadeiras[4]}\n6 - ❌{listaBrincadeiras[5]}\n===============\nEscolha => "))
escolhaComida = int(input(f"===== COMIDAS 😋 =====\nEscolha uma das comidas a seguir:\n1 - 🍮 {listaComidas[0]}\n2 - 🥔 {listaComidas[1]}\n3 - 🍿 {listaComidas[2]}\n4 - 🌶 {listaComidas[3]}\n5 - 🍦 {listaComidas[4]}\n6 - ❌ {listaComidas[5]}\n===============\nEscolha => "))          