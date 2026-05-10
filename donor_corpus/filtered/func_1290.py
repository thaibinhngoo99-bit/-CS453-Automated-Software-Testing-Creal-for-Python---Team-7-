def question_checker(phrase, char_type):
    """Check if the user inserts a valid value on the upper case and symbols question.
        Then append the specific char type list if he answer is "Yes"
    """
    while True:
        print('')
        print(phrase)
        answer = input().strip().capitalize()
        if answer == 'Yes' or answer == 'No':
            break
        else:
            print('\nInvalid Value.\n')

    def char_assignment(char_check, char_type):
        if char_check == 'Yes':
            return CHAR_TYPES.append(char_type)
        else:
            pass
    char_assignment(answer, char_type)