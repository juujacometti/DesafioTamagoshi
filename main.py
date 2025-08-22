from Tamagoshi_julya import *

# ====== Funcionamento do jogo ======
def main():
    # Interações iniciais
    print(f"{25 * '='}\n  🌱🌬️  PET VIRTUAL 💧🔥 \n")
    nomeUsuario = input("Olá! Qual o seu nome? ")

    print(f"Seja bem-vindo(a) {nomeUsuario}!\nVamos criar o seu bichinho virtual!\n")
    nome = input("=> Informe o nome do seu novo pet: ")

    print("Que nome lindo!\n\nAgora, escolha a raça dele(a):")
    escolhaRaca = int(input(f"=> Escolha a raça de {nome}:\n\n1 - Aquati (Água 💧)\n  * Possui vantagem com as brincadeiras\n  * Necessidade especial: Hidratação\n\n2 - Fuegui (Fogo 🔥)\n  * Possui vantagem com a alimentação\n  * Necessidade especial: Calor\n\n3 - Ari (Ar 💨)\n  * Possui vantagem com\n  * Necessidade especial: Refrescancia\n\n4 -\n\nInforme sua escolha (1, 2, 3 ou 4): "))
    
    # Condição para raça específica
    if escolhaRaca == 1:
        pet = Aquati(nome)
    elif escolhaRaca == 2:
        pet = Fuegui(nome)

    print("...")
    print("...")
    print("Seu pet chegou!")

    pet.statusPet()


    # Looping principal do jogo
    while True:
        
        print("\nO que deseja fazer agora?")
        pet.acoes()
        escolhaAcao = int(input(f"===== AÇÕES =====\nO que você deseja fazer agora?\n1 - 🍳 {listaAcao[0]}\n2 - 🎈 {listaAcao[1]}\n3 - 🕓 {listaAcao[2]}\n{listaAcao[3]}\n5 - 🔋 {listaAcao[4]}\n6 - ❌ {listaAcao[5]}\nEscolha => "))
        
        if escolhaAcao == 1:
            escolhaComida = int(input(f"===== COMIDAS 😋 =====\nEscolha uma das comidas a seguir:\n1 - 🍮 {listaComidas[0]}\n2 - 🥔 {listaComidas[1]}\n3 - 🍿 {listaComidas[2]}\n4 - 🌶 {listaComidas[3]}\n5 - 🍦 {listaComidas[4]}\n6 - ❌ {listaComidas[5]}\n===============\nEscolha => "))
            pet.alimentar(escolhaComida)

        elif escolhaAcao == 2:
            escolhaBrincadeiras = int(input(f"===== BRINCADEIRAS 😁 =====\nEscolha uma das brincadeiras a seguir:\n1 - 🏊‍♀️ {listaBrincadeiras[0]}\n2 - 🏰 {listaBrincadeiras[1]}\n3 - 🪁 {listaBrincadeiras[2]}\n4 - 🤾‍♀️ {listaBrincadeiras[3]}\n5 - 🎮 {listaBrincadeiras[4]}\n6 - ❌{listaBrincadeiras[5]}\n===============\nEscolha => "))
            pet.brincar(escolhaBrincadeiras)
        elif escolhaAcao == 3:
            pet.tempoPassando()
        elif escolhaAcao == 4:
            if isinstance(pet, Aquati):
                pet.hidratar()
            elif isinstance(pet, Fuegui):
                pet.esquentar()
        elif escolhaAcao == 5:
            pet.statusPet()
        elif escolhaAcao == 6:
            pet.dormir()
        

    




main()
