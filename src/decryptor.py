from cryptography.fernet import Fernet
from os import rename
from os.path import splitext
from print_action import print_decryption, print_decrypt_file

# Function for decrypt a directory
def decrypt_dirs(key=None,lst_dir=[],silent=False):
    print_decryption(silent)
    if len(lst_dir) > 0 and key != None:
        for index_dir in lst_dir:
                for lst_files,dir in index_dir.items():
                    if len(dir) > 0:
                        for file in index_dir[lst_files]:
                            status = decrypt_file(file=file,key=key,silent=silent)
                            print_decrypt_file(result=status,file=file,silent=silent)
                    else:
                        if silent == False:
                            print("""[X] {}
                            NO FILES TO DECRYPT -- ENCRYPTION DISABLED!!""".format(lst_files))
        if silent == False:
            print("*** STOPING STOCKHOLM ***")

# Function for decrypt a file
def decrypt_file(file,key,silent=False):
    try:
        # Module Fernet to decrypt
        fern = Fernet(key)
        with open(file,"rb") as target_r: 
            encrypted_data = target_r.read()
        # Data decrypted from file
        decrypt_data = fern.decrypt(encrypted_data)
        # Write decrypted data on file
        with open(file,"wb") as target_w:
            target_w.write(decrypt_data)
        # Rename the file
        name,ext = splitext(file)
        if ext == ".ft":
            rename(file,name)
        return True
    except Exception:
        return False