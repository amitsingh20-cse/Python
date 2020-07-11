import PyPDF2 as pd

words = ""
filename = input('Path to the file: ')

file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not encryted! You can successfully open it!')

else:
    for i in range(1,9):
        for j in range(1,9):
            for k in range(1,9):
                for a in range(97, 123):
                    for b in range(97, 123):
                        for c in range(97, 123):
                            words = str(i) + str(j) + str(k) + chr(a) + chr(b) + chr(c)

    for i in range(len(words)):
        word = words[i]
        print('Trying dencryption by: {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('Success! The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print('Passwords tried: ' + str(tried))
            continue
