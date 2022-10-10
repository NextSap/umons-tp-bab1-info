from userInput import *
from hangmanui import *


def main_function():
    print("\n\n\nPour jouer au pendu, il faut être deux joueurs.\n")
    first_player = input("Entrez le nom du premier joueur:\n").upper()
    second_player = input("Entrez le nom du deuxième joueur:\n").upper()

    word = ask_word_in_dictionnary(second_player)

    tried_letters = []
    hidden_word = []
    cut_word = []
    max_chances = 10

    for i in range(len(word)):
        hidden_word.append("_")
        cut_word.append(word[i])

    print("Le mot a bien été pris en compte")

    chances = max_chances

    while hidden_word != cut_word:
        if chances == 0:
            print("Vous avez perdu")
            break

        print("Nombre de chances(s) restante(s) :", chances)
        print("Lettre(s) déjà jouée(s) :", str(tried_letters).replace("[", "").replace("]", "").replace("'", ""))
        print(str(hidden_word).replace(", ", "").replace("[", "").replace("]", "").replace("'", ""))

        letter = ask_letter(tried_letters, first_player)

        if (not isinstance(letter, str)) or (len(letter) != 1) or letter == " ":
            print("'" + str(letter) + "'", "n'est pas une lettre")
            continue

        tried_letters.append(letter)

        if letter in cut_word:
            for i in range(len(cut_word)):
                if letter == cut_word[i]:
                    hidden_word[i] = letter
            print("'" + str(letter) + "'", "est une bonne lettre")
        else:
            print("'" + str(letter) + "'", "n'est pas une bonne lettre")
            draw_hangman(max_chances - chances - 1)
            chances = chances - 1

    else:
        letters_without_duplicates = []
        for i in range(len(hidden_word)):
            if hidden_word[i] not in letters_without_duplicates:
                letters_without_duplicates.append(hidden_word[i])

        tried_letters_without_right_letters = []
        for i in range(len(tried_letters)):
            if tried_letters[i] not in hidden_word:
                tried_letters_without_right_letters.append(tried_letters[i])

        score = len(letters_without_duplicates) + chances - len(tried_letters_without_right_letters)
        max_score = len(letters_without_duplicates) + max_chances

        print("Vous avez gagné")
        print("Votre score est de", str(score) + "/" + str(max_score))
        return


main_function()
