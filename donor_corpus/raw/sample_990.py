import string
import random

# --- Defining Variables ---

LOWER_ALPHABET = list(string.ascii_lowercase)
DIGITS = list(string.digits)
UPPER_ALPHABET = list(string.ascii_uppercase)

SYMBOLS = list(string.punctuation)
SYMBOLS_DELETE = ['"', "'", "(", ")", ",", ".", ":", ";", "[", "]", "|", "`", "{", "}"]
for x in SYMBOLS_DELETE:
  SYMBOLS.remove(x)

CHAR_TYPES = [LOWER_ALPHABET, DIGITS] # characters used as default

# --- PROGRAM INTRO ---

print("""    
#############################################################
#                  --- Password Generator ---               #
#############################################################
#                       Language: Python                    #
#############################################################
#                                                           #
#          This is my very first project with Python        #
#   Lowercase characteres and digits are used as default    #
#                                                           #
#############################################################
""")



# --- LENGTH QUESTION ---

while True:
  print("Password Length (Min: 8 / Max: 48):")
  pass_len = input()
  try:
    pass_len = int(pass_len)
    if pass_len >= 8 and pass_len <= 48:
        break
    else:
        print("\nYou should insert a number between 8 and 16.\n")
  except ValueError:
    # In case of the user insert a value that cannot be turned into a 'int' type
    
    print("\nYou should insert a NUMBER between 8 and 16.\n")

# --- UPPERCASE AND SYMBOLS QUESTION FUNCTION ---

def question_checker(phrase, char_type):
    """Check if the user inserts a valid value on the upper case and symbols question.
        Then append the specific char type list if he answer is "Yes"
    """

    while True:
        print("")
        print(phrase)
        answer = input().strip().capitalize()
        if answer == "Yes" or answer == "No":
            break
        else:
            print("\nInvalid Value.\n")

    def char_assignment(char_check, char_type):
        if char_check == "Yes":
            return CHAR_TYPES.append(char_type)
        else:
            pass

    char_assignment(answer, char_type)


# --- ASSIGNING UPPERCASE AND/OR SYMBOLS CHARACTERS INTO THE CHAR_TYPES LIST. ---

question_checker("Do you want uppercase letters? [Yes/No]", UPPER_ALPHABET)
question_checker("Do you want symbols? [Yes/No]", SYMBOLS)

# --- CREATE THE PASSWORD ---

def create_password():
    password_list = []

    for x in range(len(CHAR_TYPES)):
        password_list.append(CHAR_TYPES[x][random.randrange(len(CHAR_TYPES[x]))]) # making at least one of all the char types appear in the password

    for x in range(pass_len - len(CHAR_TYPES)):
        random_chartype = random.randrange(len(CHAR_TYPES))
        password_list.append(CHAR_TYPES[random_chartype][random.randrange(len(CHAR_TYPES[random_chartype]))]) # the spaces that remained will be filled with random characteres


    random.shuffle(password_list)
    password = "".join(password_list)

    return password

# --- SHOW OUTPUT ---

def show_password():
    print("\n")
    print(f"Password: {create_password()} ")
    print("\n")


show_password()

# --- REMAKE THE PASSWORD ---

while True:
    print("Remake the password? [Yes/No]")
    answer = input().strip().capitalize()
    if answer == "Yes" or answer == "No":
        if answer == "Yes":
            show_password()
        else:
            print("\n")
            break
    else:
        print("\nInvalid Value.\n")