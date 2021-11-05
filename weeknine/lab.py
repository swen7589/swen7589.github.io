from zipfile import ZipFile
with ZipFile('guido_secrets.zip') as zf:
    password = b'BFDL'
    zf.extractall(pwd=password)

