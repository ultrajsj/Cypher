message = input("Input any message : ")
translated = ""

i = len(message) - 1
while i>=0:
    translated += message[i]
    i = i - 1

print(translated)