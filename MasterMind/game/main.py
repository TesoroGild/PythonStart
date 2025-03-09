from mastermind import *

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
