from django.forms import modelformset_factory
import pyperclip

def main():
    my_key = 8
    my_message = 'common sense is not common.'

    ciphertext = encryptMessage(my_key, my_message)
    print(ciphertext + '|')

    pyperclip.copt(ciphertext)


def encryptMessage(key, message):
    pass


if __name__='__main__':
    main()