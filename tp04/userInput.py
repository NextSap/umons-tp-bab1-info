def belongs_to_dictionnary(word: str):
    with open("words.txt", "r", encoding="UTF-8") as file:
        word_list = file.read().splitlines()
        return word in word_list


def ask_word_in_dictionnary(player_name: str):
    word = ""
    while not belongs_to_dictionnary(word):
        word = input(player_name + " doit entrer un mot à trouver :\n").upper()

    return word


def ask_letter(tried_letters: list, player_name: str):
    letter = input(player_name + " doit entrer une lettre\n").upper()

    while letter in tried_letters:
        print("Erreur: La lettre", letter, "a déjà été entrée", end="\n")
        letter = input(player_name + " doit entrer une lettre\n").upper()
    else:
        return letter
