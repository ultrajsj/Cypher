import pyperclip

def main():
    my_key = 8
    my_message = 'common sense is not so common.'

    ciphertext = encryptMessage(my_key, my_message)
    print(ciphertext + '|')

    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    grid = [''] * key

    for i in range(key):
        pointer = i

        while pointer < len(message):
            grid[i] += message[pointer]
            pointer += key
    
    return ('').join(grid)

if __name__=='__main__':
    main()