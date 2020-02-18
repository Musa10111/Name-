#Your Name In Japannese
import sys

JAPANESE_ALPHABETS = {"A": 'Ka', "B": 'zu', "C": 'mi', "D": 'te', "E": 'ku', "F": 'lu', "G": 'ji', "H": 'ri', 
"I": 'ki', "J": 'zu', "K": 'me', "L": 'ta', "M": 'rin', "N": 'to', "O": 'mo', "P": 'no', "Q": 'ke', "R": 'shi', 
"S": 'ari', "T": 'chi', "U": 'do', "V": 'ru', "W": 'me', "X": 'na', "Y": 'fu', "Z": 'zi'}


def get_users_name():
#prompts the user to type in name
    name = input("Enter Your name: ").upper()
    return name



def play_again():
#ask if want to translate another name or terminate programe
    print("\nDo want to check another name? (yes or no)")
    return input().lower().startswith("y")



def is_all_letters(name):
#check if user entered letters only, if not start again or end
    return name.isalpha()


def get_japannese_name(name):
#get transleted name
    translated = ""
    for letter in name:
        for eng, jpy in JAPANESE_ALPHABETS.items():
            if letter == eng:
                translated += jpy
    print(f"You name in Japanese is {translated}")


print()
while True:
    name = get_users_name()
    if is_all_letters(name):
        get_japannese_name(name)
    else:
        print("Your name must have letters only!")
    if not play_again():
        break

