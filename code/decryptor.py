from cryptography.fernet import Fernet
from os import system, rename
from os.path import splitext
from time import sleep

# Funcion verbose mode
def print_decryption(silent=False):
    if silent == False:
        system('clear')
        print("""
            **************************************
            *|      STARTING DECRYPTION!!!      |*
            **************************************\n""")
        sleep(0.5)
        print("*** DECRYPTING FILES ***")
        sleep(2)

# Funcion que descifra un directorio
def decrypt_dirs(key=None,lst_dir=[],silent=False):
    print_decryption(silent)
    if len(lst_dir) > 0 and key != None:
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    if len(dir) > 0:
                        for file in index_dir[lst_files]:
                            status = decrypt_file(file=file,key=key,silent=silent)
                            if silent == False and status == True:
                                print("[$] -> FILE DECRYPTED {:>35}"
                                .format(file.replace(lst_files+"/", "").replace('.ft',""), end=""))
                                sleep(0.2)
                    else:
                        if silent == False:
                            print("NO FILES TO ENCRYPT -- ENCRYPTION DISABLED!!")
        if silent == False:
            print("*** STOPING STOCKHOLM***")


# Funcion de descifrado de archivo
def decrypt_file(file,key,silent=False):
    try:
        fern = Fernet(key)
        with open(file,"rb") as target_r:
            encrypted_data = target_r.read()
        decrypt_data = fern.decrypt(encrypted_data)
        with open(file,"wb") as target_w:
            target_w.write(decrypt_data)
        f,ext = splitext(file)
        if ext == ".ft":
            rename(file,f)
        return True
    except ValueError:
        if silent == False:
            print("[X] -> ERROR KEY TO FILE {} - TRY OTHER KEY\n"
            .format(file), end="")
            sleep(0.2)
        return False
    except Exception:
        if silent == False:
            print("[X] -> ERROR DECRYPT {:>35}\n"
            .format(file), end="")
            sleep(0.2)
        return False