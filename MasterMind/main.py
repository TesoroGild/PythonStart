####################
#      IMPORT      #
####################
import random



####################
#     FONCTIONS    #
####################
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
    print("Merci d'avoir joué et à bientôt!!!")
    exit()

def mastermind():
    #Possible ways to generate the systeme_combinaison
    #systeme_combinaison = [random.choice(colors) for i in range(4)]
    #print(systeme_combinaison)
    combinaison_length = length_choice()
    systeme_combinaison = random.choices(colors, k = combinaison_length)
    is_user_input_valid = False
    while not is_user_input_valid:
        user_choice = input(f"Veuillez choisir une combinaison de {combinaison_length} lettres entre B, R, Y et W : ")
        user_combinaison = list(user_choice)
        if len(user_combinaison) != combinaison_length:
            print(f"Combinaison de longueur {combinaison_length} requise.")
        else:
            is_user_input_valid = user_combinaison_validation(combinaison_length, user_combinaison)
    combinations_comparison(systeme_combinaison, user_combinaison)

def length_choice():
    combinaison_length = input("Quelle longueur souhaitez-vous pour les combinaisons de cette partie? (Minumum 4) : ")
    while True:
        if combinaison_length.isdigit():
            tmp = int(combinaison_length)
            if tmp < 4:
                combinaison_length = input("Veuillez entrer un nombre >= 4 : ")
            else:
                return tmp
        else:
            combinaison_length = input("Veuillez entrer un nombre >= 4 : ")

def user_combinaison_validation(combinaison_length, user_combinaison):
    for i in range(combinaison_length):
        if user_combinaison[i].upper() not in colors:
            print("Seuls les lettres B, R, Y et W sont autorisées.")
            return False
    return True

def color_match_check():
    print("color_match_check To Do...")

def position_match_check():
    print("position_match_check To Do...")

def combinations_comparison(systeme_combinaison, user_combinaison):
    print("combinations_comparison : Next step...")
    color_match_check()
    position_match_check()



####################
#       MAIN       #
####################
welcome()
continue_loop = True
colors = ["B", "R", "Y", "W"]
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
    mastermind()