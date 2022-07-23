from os import listdir
from os.path import isdir, isfile, splitext
from getpass import getuser
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
# Rutas de Directorio del usuario
user_target = getuser()
user_dir = '/home/'+user_target
default_dir = '/home/'+user_target+'/infection'
# Diccionario de extensiones afectadas por Wannacry
src_dic = set()
# Referencias de archivos y directorios afectados
target_dir = []
target_files = []
error_files = []

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

# Funcion Verbose del programa - Salida por consola
def print_scan():
    print(banner)
    sleep(0.5)
    print("""
        **************************************
        *|    SCANNING FILES TO INFECT!!!   |*
        **************************************\n""")
    sleep(0.5)
    print("""*** SCANNING RESULT ***
    """)
    num_files = 0
    num_directories = 0
    num_error = 0
    for dir in target_files:
        num_directories = num_directories+1
        for d,file in dir.items():
            sleep(0.2)
            print("* DIRECTORY TO INFECT --> {}".format(d.replace(user_dir,"")))
            for f in file:
                num_files = num_files+1  
                sleep(0.2)
                print("[*]-- FILE TO INFECT   --> {:>35}".format(f.replace(d+'/',"")))
        print()
    for file in error_files:
                print("[X]-- ERROR FILE - NO AFECTED   --> {:>35}".format(file))
                num_error = num_error+1
    print()
    print("""-_- DIRECTORIES AFFECTED -_-
    {}""".format(num_directories))
    print("""-*- FILES AFFECTED -*-
    {}""".format(num_files))
    print("""-X- ERROR FILES - NO AFFECTED -*-
    {}""".format(num_error))

# Funcion de listado/escaneo de Directorio y Subdirectorios
def scan_dir(dir=None, silent=False):
    if dir == None:
        dir = default_dir
    try:
        target_dir.append(dir)
        files = []
        # Escaneo de directorios
        for obj in listdir(dir):
            if isfile(dir+'/'+obj):
                # Se obtiene extension
                file, ext = splitext(dir+'/'+obj)
                # Verificacion de extension [Diccionario Cargado]
                if ext in src_dic: 
                    files.append(dir+'/'+obj)
                else:
                    error_files.append(dir+'/'+obj)
                del file     
        directory = {dir:files}
        target_files.append(directory)
        # Escaneo de subdirectorios
        for obj in listdir(dir):
            if isdir(dir+'/'+obj):
                scan_dir(dir+'/'+obj)
    except:
        if silent == False:
            print("ERROR READ DIRECTORY -> {}".format(dir))

# Funcion de inicio del programa
def scan_files(silent):
    get_dictionary(silent=silent)
    scan_dir(silent=silent)
    if silent == False:
            print_scan()
    return target_files
        