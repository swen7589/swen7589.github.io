
from zipfile import ZipFile

# step 3 part 1
with open('Ashley-Madison.txt', 'r', encoding='utf-8') as f:
    text = f.read()

passwords = [line.strip() for line in f]

for password in passwords:
    if password == True:
        f.extractall(pwd=password)
        print(password)
    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            text = f.read()



