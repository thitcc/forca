def zero():
    return b"                   _______\n \
                  |     | \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def one():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def two():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |     | \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def three():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |     |\ \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def four():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |    /|\ \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def five():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |    /|\ \n \
                  |      \ \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def six():
    return b"                   _______\n \
                  |     | \n \
                  |     @ \n \
                  |    /|\ \n \
                  |    / \ \n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
                  |\n \
               -------\n\n"

def underline(word, right_answers):
    underlined = "      "
    for i in word:
        if i in right_answers:
            underlined += i + " "
        else:
            underlined += "_ "

    underlined += "\n"

    return underlined.encode()