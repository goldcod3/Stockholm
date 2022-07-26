from time import sleep
from os import system

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

# Funcion Verbose - Salida por consola
def print_scan(lst_dirs=None, lst_error=None):
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
    for dir in lst_dirs:
        num_directories = num_directories+1
        for d,file in dir.items():
            sleep(0.2)
            print("* DIRECTORY AFFECTED --> {}".format(d))
            for f in file:
                num_files = num_files+1  
                sleep(0.2)
                print("[*]-- FILE AFFECTED   --> {:>35}".format(f.replace(d+'/',"")))
        print()
    for file in lst_error:
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

# Function was printing encryption action
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
        print("*** ENCRYPTING FILES ***")
        sleep(2)

# Function was printing decryption action
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

# Print result of encription file
def print_encrypt_file(result=False, file=None, silent=False):
    if result == True and silent == False:
        print("""[$] -> FILE ENCRYPTED 
        {:>35}""".format(file.replace('.ft',"")+'.ft', end=""))
        sleep(0.2)
    elif result == True and silent == False:
        print("""[X] -> ERROR ENCRYPT 
        {:>35}\n""".format(file), end="")
        sleep(0.2)

# Print result of decription file
def print_decrypt_file(result=False, file=None, silent=False):
    if result == True and silent == False:
        print("""[$] -> FILE DECRYPTED 
        {:>35}""".format(file.replace('.ft',""), end=""))
        sleep(0.2)
    elif result == True and silent == False:
        print("""[X] -> ERROR DECRYPT 
        {:>35}\n""".format(file), end="")
        sleep(0.2)