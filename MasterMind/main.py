def welcome():
    print("Bienvenue au MasterMind.")
    print("Cette version a été crée dans le but d'apprendre le langage Python. Nous espérons qu'elle vous plaira.")

def menu():
    print("1. Jouer")
    print("2. Regles")
    print("3. A propos")
    print("4. Quitter")

def rules():
    print("Regles :")
    print("To Do...")

def about():
    print("A propos :")
    print("To Do...")

def exit_game():
    print("Merci d'avoir joué.")
    exit()

def mastermind():
    game_choice = "To Do..."
    user_choice = input("Veuillez choisir une combinaison de 4 chiffres : ")
    verification(user_choice)

def verification(user_choice):
    if user_choice == "1":
        print("1")
    elif user_choice == "2":
        print("2")
    elif user_choice == "3":
        print("3")
    else:
        print("4")

####################
#       MAIN       #
####################
welcome()
continue_loop = True
while continue_loop:
    try:
        menu()
        chosen_menu = input("Votre choix : ")
        if 0 < int(chosen_menu) <= 4:
            continue_loop = False
        else:
            print("Veuillez entrer un nombre entre 1 et 4.")
    except ValueError:
        print("Erreur système")

if chosen_menu == "4":
    exit_game()
if chosen_menu == "2":
    rules()
if chosen_menu == "3":
    about()
if chosen_menu == "1":
    print("1")