class Tamaghosi:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0

    # Reduz a fome proporcionalmente a quantidade real. Exemplo: se a fome for 50 e a quantidade for 50%, a fome fome será 25
    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)

    # Retorna o tédio proporcionalmente à quantidade de brincadeira
    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)

    # Retorna um número representando o humor do bichinho. Quanto menor a fome e o tédio, melhor o humor.
    def getHumor(self):
        return 100 - ((self.fome + self.tedio) / 2)

    # Diminui a saúde do bichinho conforme as condições de fome (quanto mais alta, pior)
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 60)) or ((self.tedio > 60 and self.tedio <= 60)):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 60)):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            print("Estou morrendo.......AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH 💀")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu 😭")

    def tempoPassando(self):
        self.vida() # Atualiza a saúde baseado na sua fome e tédio atuais
        self.idade += 0.2 # O tempo passa e o pet envelhece
        self.tedio += 2.5 # Aumenta o tédio com o passar do tempo
        self.fome -= 5