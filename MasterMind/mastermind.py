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
    print("""Le Mastermind ou Master Mind est un jeu de société pour deux joueurs dont le but est de trouver un code (couleur et position de 4 ou 5 pions) en 10 ou 12 coups.
          
          Le jeu se joue à deux : un codificateur et un décodeur.
          
          Le but est de deviner, par déductions successives, la couleur et la position des 4 ou 5 pions (selon les versions du jeu) cachés derrière un écran. Les débutants peuvent adopter une formule moins difficile en ne cachant que 3 ou 4 pions et en n'utilisant que 6 couleurs au lieu de 8. C'est une question de convention préalable.

          Déroulement du jeu : le codificateur pose à l'endroit prévu à cet effet, les 4 ou 5 pions de son choix. Il doit prendre soin de ne pas révéler la couleur et la répartition dans les trous des pions. Rien ne l'empêche d'en choisir plusieurs d'une même couleur. Les versions plus modernes disposent d'un système intégré qui permet cette discrétion. 
          
          Son adversaire, le décodeur, est chargé de déchiffrer ce code secret. Il doit le faire en 10 ou 12 coups au plus. Il place 4 ou 5 pions dans les trous de la première rangée immédiatement près de lui. Si l'un des pions correspond par sa position et sa couleur à un pion caché derrière l'écran, le codificateur l'indique en plaçant une fiche noire dans l'un des trous de marque, sur le côté droit correspondant du plateau. Si l'un des pions correspond uniquement par sa couleur, le Codificateur l'indique par une fiche blanche dans l'un des trous de marque. S'il n'y a aucune correspondance, il ne marque rien.
          
          Le décodeur continue de poser des pions par rangées successives. La tactique consiste à sélectionner en fonction des coups précédents, couleurs et positions, de manière à obtenir le maximum d'informations de la réponse du partenaire puisque le nombre de propositions est limité par le nombre de rangées de trous du jeu. Dans la plupart des cas, il s'efforce de se rapprocher le plus possible de la solution, compte tenu des réponses précédentes, mais il peut aussi former une combinaison dans le seul but de vérifier une partie des conclusions des coups précédents et de faire en conséquence la proposition la plus propice à la déduction d'une nouvelle information.
          
          Quand il est arrivé, au bout d'un certain nombre de coups, à placer les 4 ou 5 pions qui correspondent exactement par la couleur et la position à ceux du code, la manche est terminée.
          
          À la fin de la manche, le codificateur obtient 1 point par rangée de pions d'investigation placée par l'adversaire. Il déplace sa fiche de marque sur sa ligne de score.
          
          La partie se joue en un nombre pair de manches de façon à équilibrer les chances en inversant les rôles à la fin de chaque manche. Celui qui était codificateur devient décodeur et inversement.

          Le vainqueur est celui qui, une fois le même nombre de manches remportées, a marqué le plus de points.
          
          Il a donc fallu à son adversaire plus de coups pour déchiffrer les codes.

          La variante du jeu avec 4 pions et 6 couleurs permet 64 = 1 296 combinaisons ; celle avec 5 pions et 8 couleurs 85 = 32 768 combinaisons.

          Une autre variante permet 59 049 combinaisons : elle se joue de la même façon mais avec la possibilité de laisser des trous libres entre ses pions, ce qui équivaut à créer une neuvième couleur fictive. Il a donc la possibilité de laisser un ou plusieurs trous inoccupés derrière l'écran. Si le décodeur laisse un espace libre en face d'un pion caché, il s'est trompé et le codificateur ne pose aucune fiche. C'est comme si le décodeur avait proposé un pion ne correspondant à aucun du code secret.""")

def about():
    print("A propos :")
    print("BG Copyright 2025")

def exit_game():
    print("Merci d'avoir joué et à bientôt!!!")
    exit()

def mastermind():
    colors = ["B", "R", "Y", "P", "G", "O", "V", "W"]
    print("Les couleurs pour cette partie sont : B, R, Y, P, G, O, V, W.")
    #Possible ways to generate the system_combination
    #system_combination = [random.choice(colors) for i in range(4)]
    number_of_turns = 10 # Can be change after
    combination_length = length_choice()
    system_combination = random.choices(colors, k = combination_length)
    # Entrees de test
    # 1- G, O, V, W
    # 2- P, Y, R, B
    # 3- R, O, V, W
    # 4- B, G, O, V

    #system_combination = ["B", "B", "B", "B"]
    #system_combination = ["B", "B", "B", "O"]
    #system_combination = ["B", "B", "Y", "Y"]

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
                is_user_combination_valid = user_combination_validation(colors, combination_length, user_combination)
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

def user_combination_validation(colors, combination_length, user_combination):
    for i in range(combination_length):
        if user_combination[i].upper() not in colors:
            print("Les couleurs disponibles pour ce jeu sont B, R, Y, P, G, O, V, et W.")
            return False
    return True

def combinations_comparison(combination_length, system_combination, user_combination):
    correct_position = 0
    wrong_position = 0
    indexes_to_check = list(range(combination_length))
    for i in range(combination_length):
        # print(f"i = {i}")
        # print(user_combination[i])
        # print(system_combination[i])
        if user_combination[i].upper() == system_combination[i]:
            correct_position += 1
            indexes_to_check.remove(i)
            #indexes_to_check.pop(i)
    
    #print(f"les indices restants = {indexes_to_check}")
    system_indexes_to_check = indexes_to_check.copy()

    for i in indexes_to_check:
    #for i in range(combination_length):
        # print(f"i = {i}")
        # print(system_combination[i])
        for j in system_indexes_to_check:
            # print("1-ICI")
        #for j in range(combination_length):
            # print(f"j = {j}")
            # print(user_combination[j])
                if user_combination[i].upper() == system_combination[j]:
                    # print(f"user = {i}")
                    # print(user_combination[i])
                    # print(f"system = {j}")
                    # print(system_combination[j])
                    wrong_position += 1
                    system_indexes_to_check.remove(j)
                    # print(f"les indices system restants = {system_indexes_to_check}")
                    # print(f"les indices user restants = {indexes_to_check}")
                    #system_indexes_to_check.pop(j)
                    break
    print(f"{correct_position} couleurs bien placées et {wrong_position} couleurs mal placées.")
    return correct_position