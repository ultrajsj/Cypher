import time, os, sys, transpositionDecrypt, transpositionEncrypt

def main():
    inputFilename = 'frankenstein.txt'
    outputFilename = inputFilename[:-4] + '.encrypted.txt'

    myKey = 10
    myMode = 'encrypt'

    if not os.path.exists(inputFilename):
        print('The file %s does not exits.' % (inputFilename))
        sys.exit()
    
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s.' % (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing' % (myMode.title()))  #Title()?

    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sion %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


if __name__=='__main__':
    main()
