# Transposition Cipher Decrypt Program

import math, pyperclip

def main():
    my_message = 'Cenoonommstmme oo snnio. s s c'
    my_key = 8

    plain_text = decryptMessage(my_key, my_message)

    print(plain_text + "|")
    pyperclip.copy(plain_text)


def decryptMessage(key, message):
    #First, caculating some values
    #Length of columns for using transposition grid
    num_of_columns = int(math.ceil(len(message) / float(key)))

    #Length of rows for using transposition grid
    num_of_rows = key

    #Number of boxes to fill in the last column of the grid
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    #Each string of plaintext in one column of the grid
    plaintext = [''] * num_of_columns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1
    
    return(''.join(plaintext))


if __name__=='__main__':
    main()