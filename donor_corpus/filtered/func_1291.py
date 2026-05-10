def create_password():
    password_list = []
    for x in range(len(CHAR_TYPES)):
        password_list.append(CHAR_TYPES[x][random.randrange(len(CHAR_TYPES[x]))])
    for x in range(pass_len - len(CHAR_TYPES)):
        random_chartype = random.randrange(len(CHAR_TYPES))
        password_list.append(CHAR_TYPES[random_chartype][random.randrange(len(CHAR_TYPES[random_chartype]))])
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password