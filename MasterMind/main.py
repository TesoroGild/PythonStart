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