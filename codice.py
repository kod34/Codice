#!/usr/bin/env python3
import os
from mods.functions import *
from mods.args import *

crypt_list = ['RSA','ELG','DSA','ECDH','ECDSA','EDDSA','IDEA','3DES','CAST5','BLOWFISH','AES','AES192','AES256','TWOFISH','CAMELLIA128','CAMELLIA192','CAMELLIA256']

if args.crypt != None and args.user != None and args.app != None and args.len != None and args.out != None:
    if crypt not in crypt_list:
        sys.exit(color.RED+"[-] Invalid algorithm")
    try:
        int(args.len)
    except (ValueError) as e:
        sys.exit(color.RED+str(e))
    print(banner)
    
    if '.gpg' == os.path.splitext(outf)[1]:
        if not os.path.exists(outf):
            sys.exit(color.RED+"[-] Invalid path")
        decrypt_f()
        gen_pass()
        store()
        crypt_f()
    else:
        gen_pass()
        store()
        crypt_f()
        
    print(color.GREEN+"[*] Password saved to "+color.YELLOW+os.path.splitext(outf)[0]+'.gpg')

else:
    parser.error("A required argument is missing")
