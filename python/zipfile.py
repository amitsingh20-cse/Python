import zipfile
from tqdm import tqdm

f = open("password.txt", "w")
for i in range(1, 9):
    for j in range(1, 9):
        for k in range(1, 9):
            for a in range(97, 123):
                for b in range(97, 123):
                    for c in range(97, 123):
                        words = str(i) + str(j) + str(k) + chr(a) + chr(b) + chr(c)
                        f.write("%s\n" % words)
f.close()
wordlist = "password.txt"
zip_file = "Task.zip"
zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
