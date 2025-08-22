# COISAS FALTANTES 
# definição das duas racas (yasme)
# o benefício das outras 2 raças (yasme)
# os desafios (função dormir realizada, falta a de acordar e linkar elas) (julya e yasme) 
# definição de função de vida, tempo (yasme)
# chamar todas as funções para funcionamento do jogo e incluir coisas que você alterar

# ====== Listas para o funcionamento do jogo ======
                    # Água            Terra               Ar                Fogo               
listaBrincadeiras = ["Ir na piscina", "Castelo de areia", "Soltar pipa", "Jogar queimada", "Video game", "Cancelar escolha"]
listaComidas = ["Gelatina", "Batata", "Pipoca", "Pimenta", "Sorvete", "Cancelar alimentação"]
listaAcao = [f"Alimentar", "Brincar", "Passar o tempo", "Necessidade da raça", "Status do pet", "Sair (o pet irá dormir)"]


# ====== Classe mãe ======
class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50 
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.dormindo = False
        
    def statusPet(self):
        print(f"\n{25 * '='}\nSTATUS DE: {self.nome}")
        print(f"😋 Fome: {self.fome}")
        print(f"😷 Saúde: {self.saude}")
        print(f"🙄 Tédio: {self.tedio}")
        self.humor()
        print(f"📏 Idade: {self.idade}")
        if isinstance(self, Aquati):
            print(f"💧 Hidratação: {self.hidratacao}")
        elif isinstance(self, Fuegui):
            print(f"Calor: {self.calor}")
            
            
    def acoes(self): 
        if isinstance(self, Aquati):
            listaAcao[3] = "4 - 💧 Hidratar"
        elif isinstance(self, Fuegui):
            listaAcao[3] = "4 - 🔥 Esquentar"
        
        
        


    # Verifica as condições da brincadeira
    def brincar(self, escolhaBrincadeira):
        if (self.tedio >= 0) and (self.tedio <= 100):    # Verifica o nível de tédio           
            if escolhaBrincadeira in [1, 2, 3, 4]:
                self.tedio = max(0, self.tedio - 15)
            elif escolhaBrincadeira == 5:
                self.tedio = max(0, self.tedio - 10)
            elif escolhaBrincadeira == 6:
                print("Brincadeira cancelada")
        else:
            print(f"{self.nome} não está com tédio.") 
        print(f"Nível de tédio: {self.tedio}")    # Informação para o usuário

    
    # Verifica as condições de alimentação
    def alimentar(self, escolhaComida):
        if (self.fome >= 0) and (self.fome <= 100):    # Verifica o nível de fome
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
            print("🙄 Humor: Triste 😭")
        elif humor <= 50:
            print("🙄 Humor: Estável 😐")
        elif humor <= 75:
            print("🙄 Humor: Bem ☺️")
        else:
            print("🙄 Humor: Muito feliz! 😁")
            
            
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
        self.fome += 5


# ====== Criação de raças ======
#Raça de água
class Aquati(Tamagoshi): 
    def __init__(self, nome):
        super().__init__(nome)    # Chamada do construtor da classe mãe  
        self.hidratacao = 100    # Definição de atributos específicos da raça

    def brincar(self, escolhaBrincadeira):
        if escolhaBrincadeira == 1:    # Brincadeira que envolve água diminui o tédio mais rápido
            self.tedio = max(0, self.tedio - 30)    # Garante que o valor não seja negativo, caso fique, será substituído para zero
            print(f"{self.nome} fez sua brincadeira favorita! 🤩")
        elif escolhaBrincadeira in [2, 3, 4]:    # Brincadeiras 'favoritas' de outras raças
            self.tedio = max(0, self.tedio - 15)
        elif escolhaBrincadeira == 5:    # Brincadeira genérica
            self.tedio = max(0, self.tedio - 10)
        elif escolhaBrincadeira == 6:    # Cancelar escolha de brincadeiras
            print("Brincadeira cancelada.")

    def nadar(self):
        self.tedio -= 15
        self.hidratacao += 10
        print(f"{self.nome} nadou e está mais feliz! 🐟")

    # Necessidade específica da raça
    def hidratar(self):
        self.hidratacao += 25
        print(f" {self.nome} bebeu água! 💧")



# Raça de fogo
class Fuegui(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)    # Chamada do construtor da classe mãe
        self.calor = 100    # Definição de atributos específicos da raça

    def alimentar(self, escolhaComida):
        if escolhaComida in [1, 2, 3]:
            self.fome = max(0, self.fome - 15)
        elif escolhaComida == 4:
            self.fome = max(0, self.fome - 25)
            print(f"{self.nome} comeu sua comida favorita! 🤩")
        elif escolhaComida == 5:
            self.fome = max(0, self.fome - 10)
        elif escolhaComida == 6:
            print("Alimentação cancelada.")

     # Necessidade específica da raça
    def esquentar(self):
        self.calor += 25
        print(f"{self.nome} se esquentou e se sente melhor! ♨️")

    def soltarFogo(self):
        self.tedio -= 30
        self.energia -= 20
        print(f"{self.nome} soltou fogo! 🔥")



# Raça de ar
class Ari(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.refrescancia = 20 # MUDAR!

    def pipar(self):
        self.refrescancia += 30
        self.tedio = max(0, self.tedio - 20)  # Correr alivia o tédio | '0' é para que pare de tirar quando o tédio atingir 0
        print(f"{self.nome} soltou pipa ao AR livre e se sente melhor! 🍃")

    def planar(self):
        self.tedio = max(0, self.tedio - 20)
        self.idade += 0.5
        print(f"{self.nome} planou no céu e se sente melhor! ☁️")



# Raça de terra
class Terru(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.resistencia = 100  # Atributo especial da raça

    def conexaoNatureza(self):
        if self.fome <= 80:
            self.saude = min(100, self.saude + 25)
            self.tedio = max(0, self.tedio - 10)
            print(f"{self.nome} se conectou com a natureza e se sente renovado! 🌱")
        else:
            print(f"{self.nome} está com fome demais para se concentrar! 🍽️")


    def muralhaPedra(self):
        self.saude = min(100, self.saude + 10)
        self.idade = max(0, self.idade - 0.2)
        print(f"{self.nome} criou uma muralha protetora e ganhou tempo! 🧱")
        
        
# Raça de ar
# Da um nome diferentinho pras raças 

# Raça de terra

        
