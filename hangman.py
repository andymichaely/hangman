def choose_word(file_path, index):
    count1 = 0
    j = 0
    word_list2 = []
    num_of_words = 0
    text2 = open(file_path, 'r')
    text = text2.read()
    word_list = text.split()
    if index > len(word_list):
        word_r = word_list[index - len(word_list) - 1]
    else:
        word_r = word_list[index - 1]
    for x in word_list:
        count1 = word_list.count(x)
        if x not in word_list2:
            word_list2.append(x)
            count1 = 0
        else:
            count1 = 0

    num_of_words = len(word_list2)
    return word_r
    text.close()


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0: "x-------x",
                      1: """x-------x
        |
        |
        |
        |         
                 """,
                      2: """x-------x
        |        
        0        
        |
        |
        |""",
                      3: """x-------x
        |
        0
        |
        |
        | 
                """,
                      4: """x-------x
        |
        0
       /|\\
        |
        |
                """,
                      5: """x-------x
        |
        0
       /|\\
       /
        | 
                """,
                      6: """x-------x
        |
        0
       /|\\
       / \\
        |
         """}
    return (HANGMAN_PHOTOS[num_of_tries])


def show_hidden_word(secret_word, old_letters_guessed):
    for i in range(0, len(secret_word)):
        if (secret_word[i] not in old_letters_guessed):
            secret_word = secret_word.replace(secret_word[i], "_")
    secret_word = " ".join(secret_word)
    return secret_word


def check_valid_input(letter_guessed, old_letters_guessed):
    if (letter_guessed.isalpha()) and (len(letter_guessed) == 1) and (letter_guessed not in old_letters_guessed):
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if (check_valid_input(letter_guessed, old_letters_guessed) == True):
        old_letters_guessed.append(letter_guessed)
        return True
    elif (letter_guessed.upper == letter_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    elif (letter_guessed.lower == letter_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    elif (letter_guessed.isalpha() == False):
        return ("X")
    else:
        old_letters_guessed.sort()
        old_letters_guessed2 = ' -> '.join(old_letters_guessed)
        print(old_letters_guessed2)
        return False


def check_win(secret_word, old_letters_guessed):
    word = show_hidden_word(secret_word, old_letters_guessed)
    if (word.find('_') == -1):
        return True
    return False


def check_if_letter_in_secret_words(letter_guessed, secret_word):
    if ((letter_guessed in secret_word) == True):
        return True
    else:
        return "):"


def main():
    HANGMAN_ASCII_ART = (""" | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")
    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART, '\n', "max tries:", MAX_TRIES)
    file_p = input("enter file path ")
    secret_word = choose_word(file_p, int(input("enter index ")))
    num_of_tries = 0
    is_leagal = None
    old_letters_guessed = []
    print("Lets start the game!")
    print(print_hangman(num_of_tries))
    print(show_hidden_word(secret_word, old_letters_guessed))
    is_won = False
    while (num_of_tries <= 6 and is_won == False):
        letter_guessed = input("Guess a letter:")
        letter_guessed = letter_guessed.lower()
        is_leagal = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if (is_leagal == "X"):
            print(is_leagal)
        elif (is_leagal == True):
            if (check_if_letter_in_secret_words(letter_guessed, secret_word) == True):
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                print("):")
                num_of_tries = num_of_tries + 1
                print(try_update_letter_guessed(letter_guessed, old_letters_guessed))
                print(print_hangman(num_of_tries))
        if (check_win(secret_word, old_letters_guessed) == True):
            print("WON")
            print()
            break
        if (check_win(secret_word, old_letters_guessed) == False and num_of_tries == MAX_TRIES):
            print("LOSE")
            print()
            break


if __name__ == "__main__":
    main()


