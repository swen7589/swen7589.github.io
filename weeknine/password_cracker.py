
from zipfile import ZipFile

main_file = 'Ashley-Madison.txt'
zip_file = "whitehouse_secrets.zip"

with open(main_file, 'rb', encoding='utf-8') as passwords:
    all_passwords = passwords.readlines()
    num_passwords = len(all_passwords)

the_zip = zipfile.ZipFile(zip_file)

for index, password in enumerate(all_passwords):
    try: 
        the_zip.extractall(path="Extracted Folder", pwd=password.strip())
        print("PASSWORD CRACKED")
        print("PASSWORD: ", password.decode().strip())
        break
    except:
            
            print(f"SCAN COMPLETE {round((index/num_passwords)*100, 2)}%")
            print(f"TRYING AGAIN {password.decode().strip()} ")
            continue

