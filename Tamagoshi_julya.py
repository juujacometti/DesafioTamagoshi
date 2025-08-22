import json # Para salvar o histórico do bichinho no JSON


# ====== Listas para o funcionamento do jogo ======
                    # Água            Terra               Ar                Fogo               
listaBrincadeiras = ["Ir na piscina", "Castelo de areia", "Soltar pipa", "Jogar queimada", "Video game", "Cancelar escolha"]
listaComidas = ["Gelatina", "Batata", "Pipoca", "Pimenta", "Sorvete", "Cancelar alimentação"]
listaAcao = [f"Alimentar", "Brincar", "Passar o tempo", "Necessidade da raça", "Status do pet", "Sair (o pet irá dormir)", "Apagar pet"]


# ====== Classe mãe ======
class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50 
        self.saude = 100
        self.idade = 0
        self.tedio = 50
        self.dormindo = False
        
    def statusPet(self):
        print(f"\n{25 * '='}\nSTATUS DE: {self.nome}")
        print(f"😋 Fome: {self.fome:.2f}")
        print(f"😷 Saúde: {self.saude}")
        print(f"🙄 Tédio: {self.tedio:.2f}")
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
        elif isinstance(self, Ari):
            listaAcao[3] = "4 - 💨 Refrescar"
        elif isinstance(self, Terru):
            listaAcao[3] = "4 - 🌱 Conectar à Natureza"
        
        
        


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
    # Reduz a saúde dependendo da fome e tédio
        if self.fome > 90 or self.tedio > 90:
            self.saude = 0
        elif self.fome > 80 or self.tedio > 80:
            self.saude -= 50
        elif self.fome > 60 or self.tedio > 60:
            self.saude -= 30
        elif self.fome > 50 or self.tedio > 50:
            self.saude -= 10
        
        # Garante que a saúde nunca fique negativa
        self.saude = max(0, self.saude)
        
        if self.saude == 0 or self.fome >= 100:
            print("💀 Seu bichinho morreu ⚰️")
            return True  # podemos retornar True pra indicar que morreu
        return False


            
    
    # Verifica o passar do tempo (ESTÁ IGUAL AO DA MARI, NÃO MEXI)
    def tempoPassando(self):
        morreu = self.vida()
        if morreu:
            return # Sai da função se morreu
        self.idade += 1 # O tempo passa e o pet envelhece
        self.tedio += 2.5 # Aumenta o tédio com o passar do tempo
        self.fome += 2.5


# ====== Criação de raças ======
#Raça de água
class Aquati(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.hidratacao = 50  # Necessidade especial: hidratação

    # Função especial do Aquati
    def hidratar(self):
        print(f"{self.nome} está se hidratando 💧...")
        # Aumenta hidratação (não passa de 100)
        self.hidratacao = min(100, self.hidratacao + 10)
        # Reduz o tédio (não fica menor que 0)
        self.tedio = max(0, self.tedio - 15)
        print(f"Hidratação: {self.hidratacao}, Tédio: {self.tedio}")


class Fuegui(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.calor = 50  # Necessidade especial: calor

    # Função especial do Fuegui
    def esquentar(self):
        print(f"{self.nome} está absorvendo calor 🔥...")
        # Aumenta o calor (limite 100)
        self.calor = min(100, self.calor + 10)
        # Diminui a fome (mínimo 0)
        self.fome = max(0, self.fome - 10)
        print(f"Calor: {self.calor}, Fome: {self.fome}")


class Ari(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.refrescancia = 50  # Necessidade especial: refrescância

    # Função especial do Ari
    def pipar(self):
        print(f"{self.nome} está sentindo a brisa do vento 💨...")
        # Aumenta a refrescância (até 100)
        self.refrescancia = min(100, self.refrescancia + 10)
        # Recupera um pouco da saúde (até 100)
        self.saude = min(100, self.saude + 5)
        print(f"Refrescância: {self.refrescancia}, Saúde: {self.saude}")


class Terru(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.resistencia = 50  # Necessidade especial: resistência

    # Função especial do Terru
    def conexaoNatureza(self):
        print(f"{self.nome} está se conectando com a natureza 🌱...")
        # Aumenta a resistência (até 100)
        self.resistencia = min(100, self.resistencia + 10)
        # Reduz bastante o tédio (mínimo 0)
        self.tedio = max(0, self.tedio - 20)
        print(f"Resistência: {self.resistencia}, Tédio: {self.tedio}")


# Puxando para o JSON
def salvar_estado(pet, nome_arquivo="pet.json"):
    dados = {
        "nome": pet.nome,
        "fome": pet.fome,
        "saude": pet.saude,
        "idade": pet.idade,
        "tedio": pet.tedio,
        "dormindo": pet.dormindo,
        "raca": pet.__class__.__name__,
        "extra": {}
    }

    if isinstance(pet, Aquati):
        dados["extra"]["hidratacao"] = pet.hidratacao
    elif isinstance(pet, Fuegui):
        dados["extra"]["calor"] = pet.calor
    elif isinstance(pet, Ari):
        dados["extra"]["refrescancia"] = pet.refrescancia
    elif isinstance(pet, Terru):
        dados["extra"]["resistencia"] = pet.resistencia

    with open(nome_arquivo, "w") as arq:
        json.dump(dados, arq, indent=4)



def carregar_estado(nome_arquivo="pet.json"):
    try:
        with open(nome_arquivo, "r") as arq:
            dados = json.load(arq)

            nome = dados["nome"]
            raca = dados["raca"]

            if raca == "Aquati":
                pet = Aquati(nome)
                pet.hidratacao = dados["extra"]["hidratacao"]
            elif raca == "Fuegui":
                pet = Fuegui(nome)
                pet.calor = dados["extra"]["calor"]
            elif raca == "Ari":
                pet = Ari(nome)
                pet.refrescancia = dados["extra"]["refrescancia"]
            elif raca == "Terru":
                pet = Terru(nome)
                pet.resistencia = dados["extra"]["resistencia"]
            else:
                return None

            pet.fome = dados["fome"]
            pet.saude = dados["saude"]
            pet.idade = dados["idade"]
            pet.tedio = dados["tedio"]
            pet.dormindo = dados["dormindo"]

            return pet

    except FileNotFoundError:
        return None
 