
from zipfile import ZipFile

with open('Ashley-Madison.txt', 'r', encoding='utf-8') as f:
    text = f.read()

passwords = [line.strip() for line in f]

for password in passwords:
    if password:
        f.extractall(pwd=password)
        print(password)
    try:
        with ZipFile('whitehouse_secrets.zip') as zf:
            text = zf.read()
    except RuntimeError:
        pass




