import os
from Tamagoshi import *

# ====== Função para apagar pet salvo ======
def apagar_estado():
    if os.path.exists("pet.json"):
        os.remove("pet.json")
        print("❌ Seu pet foi apagado. Você poderá criar um novo na próxima vez que jogar.")
    else:
        print("⚠️ Não existe pet salvo para apagar.")

# ====== Funcionamento do jogo ======
def main():
    # Interações iniciais
    print(f"{25 * '='}\n  🌱🌬️  PET VIRTUAL 💧🔥 \n")
    pet = carregar_estado()

    if pet:  # Se encontrou no JSON
        print(f"Bem-vindo de volta! Seu pet {pet.nome} acordou! 🌞")
        pet.acordar()
        pet.statusPet()
        rodarJogo(pet)


    else:
        nomeUsuario = input("Olá! Qual o seu nome? ")

        print(f"Seja bem-vindo(a) {nomeUsuario}!\nVamos criar o seu bichinho virtual!\n")
        nome = input("=> Informe o nome do seu novo pet: ")

        print("Que nome lindo!\n\nAgora, escolha a raça dele(a):")
        escolhaRaca = int(input(f"=> Escolha a raça de {nome}:\n\n1 - Aquati (Água 💧)\n  * Possui vantagem com as brincadeiras\n  * Necessidade especial: Hidratação\n\n2 - Fuegui (Fogo 🔥)\n  * Possui vantagem com a alimentação\n  * Necessidade especial: Calor\n\n3 - Ari (Ar 💨)\n  * Possui vantagem com saúde\n  * Necessidade especial: Refrescancia\n\n4 - Terru (Terra 🌱)\n  * Possui vantagem com as brincadeiras\n  * Necessidade especial: Resistência\n\nInforme sua escolha (1, 2, 3 ou 4): "))
        
        # Condição para raça específica
        if escolhaRaca == 1:
            pet = Aquati(nome)
        elif escolhaRaca == 2:
            pet = Fuegui(nome)
        elif escolhaRaca == 3:
            pet = Ari(nome)
        elif escolhaRaca == 4:
            pet = Terru(nome)

        print("...")
        print("...")
        print("Seu pet chegou!")

        pet.statusPet()
        rodarJogo(pet)


# Looping principal do jogo
def rodarJogo(pet):
    while True:

        # Checa se o pet já morreu
        if pet.saude <= 0 or pet.fome >= 100:
            apagar_estado()  # Apaga o JSON
            print("Você precisará criar um novo pet para continuar jogando.")
            return  # Volta para o main()
        
        print("\nO que deseja fazer agora?")
        pet.acoes()
        escolhaAcao = int(input(f"===== AÇÕES =====\nO que você deseja fazer agora?\n1 - 🍳 {listaAcao[0]}\n2 - 🎈 {listaAcao[1]}\n3 - 🕓 {listaAcao[2]}\n{listaAcao[3]}\n5 - 🔋 {listaAcao[4]}\n6 - ❌ {listaAcao[5]}\n7 - 🗑 {listaAcao[6]}\nEscolha => "))
        
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
            elif isinstance(pet, Ari):
                pet.pipar()   
            elif isinstance(pet, Terru):
                pet.conexaoNatureza()

        elif escolhaAcao == 5:
            pet.statusPet()

        elif escolhaAcao == 6:
            pet.dormir()
            print("Saindo do jogo... até logo! 🌙")
            salvar_estado(pet)
            break

        elif escolhaAcao == 7:
            apagar_estado()
            break 
        
main()
