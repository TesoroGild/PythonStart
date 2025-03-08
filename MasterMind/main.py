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
    print("Les couleurs pour cette partie sont : B, R, Y, P, G, O, V, W.")
    #Possible ways to generate the system_combination
    #system_combination = [random.choice(colors) for i in range(4)]
    number_of_turns = 10 # Can be change after
    combination_length = length_choice()
    #system_combination = random.choices(colors, k = combination_length)
    # Entrees de test
    # 1- G, O, V, W
    # 2- P, Y, R, B
    # 3- R, O, V, W
    # 4- B, G, O, V

    system_combination = ["B", "B", "B", "B"]
    #system_combination = ["B", "B", "B", "O"]
    # system_combination = ["B", "B", "Y", "Y"]

    print(system_combination)
    is_user_combination_valid = False
    while number_of_turns > 0:
        print(f"Tours restants : {number_of_turns}")
        while not is_user_combination_valid:
            user_choice = input(f"Veuillez choisir une combinaison de {combination_length} couleurs : ")
            user_combination = list(user_choice)
            if len(user_combination) != combination_length:
                print(f"Combinaison de longueur {combination_length} requise.")
            else:
                is_user_combination_valid = user_combination_validation(combination_length, user_combination)
        correct_position = combinations_comparison(combination_length, system_combination, user_combination)
        if correct_position == combination_length:
            print("Bravo, vous avez gagné!")
            break
        else:
            number_of_turns -= 1
            is_user_combination_valid = False
    if number_of_turns == 0:
        print(f"Dommage, vous avez perdu. La bonne combinaison était : {system_combination}")

def length_choice():
    combination_length = input("Quelle longueur souhaitez-vous pour les combinaisons de cette partie? (Minumum 4) : ")
    while True:
        if combination_length.isdigit():
            tmp = int(combination_length)
            if tmp < 4:
                combination_length = input("Veuillez entrer un nombre >= 4 : ")
            else:
                return tmp
        else:
            combination_length = input("Veuillez entrer un nombre >= 4 : ")

def user_combination_validation(combination_length, user_combination):
    for i in range(combination_length):
        if user_combination[i].upper() not in colors:
            print("Les couleurs disponibles pour ce jeu sont B, R, Y, P, G, O, V, et W.")
            return False
    return True

def combinations_comparison(combination_length, system_combination, user_combination):
    correct_position = 0
    wrong_position = 0
    value_checked = []
    for i in range(combination_length):
    #for i in valid_indexes:
        # print(f"i = {i}")
        # print(system_combination[i])
        find_letter = False
        j = 0
        while not find_letter and j < combination_length:
            # print("1-ICI")
        #for j in range(combination_length):
            # print(f"j = {j}")
            # print(user_combination[j])
            if j not in value_checked:
                if user_combination[i].upper() == system_combination[j]:
                    if i == j:
                        #print("********************************")
                        correct_position += 1
                    else:
                        print(f"user = {i}")
                        print(user_combination[i])
                        print(f"system = {j}")
                        print(system_combination[j])
                        wrong_position += 1
                    value_checked.append(j)
                    find_letter = True
                    j = 0
                else:
                    j += 1
            else:
                j += 1
    print(f"{correct_position} couleurs bien placées et {wrong_position} couleurs mal placées.")
    return correct_position
    



####################
#       MAIN       #
####################
welcome()
continue_loop = True
colors = ["B", "R", "Y", "P", "G", "O", "V", "W"]
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
    replay = True
    while replay:
        mastermind()
        is_replay_input_valid = False
        while not is_replay_input_valid:
            replay_input = input("Voulez-vous rejouer? (O/N) : ")
            if replay_input.upper() != "O" and replay_input.upper() != "N":
                print("Veuillez entrer O ou N.")
            else:
                is_replay_input_valid = True
                if replay_input.upper() == "N":
                    replay = False
    exit_game()
