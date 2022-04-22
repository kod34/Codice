#!/usr/bin/env python3
import os
import random
import shutil
from mods.functions import *
import mods.functions as fu
from mods.args import *

crypt_list = ['RSA','ELG','DSA','ECDH','ECDSA','EDDSA','IDEA','3DES','CAST5','BLOWFISH','AES','AES192','AES256','TWOFISH','CAMELLIA128','CAMELLIA192','CAMELLIA256']

if args.crypt != None and args.user != None and args.app != None and args.len != None and args.out != None:
    if crypt not in crypt_list:
        sys.exit(color.RED+"invalid algorithm")
    try:
        int(args.len)
    except (ValueError) as e:
        sys.exit(color.RED+str(e))
    print(banner)
    
    # if os.path.exists(outf):
    #     shutil.copyfile(outf, outf+'.backup'+str(random.randint(1,99)))
        
    # if os.path.exists(outf+'.gpg'):
    #     shutil.copyfile(outf+'.gpg', outf+'.gpg.backup'+str(random.randint(1,999)))
    
        
    if '.gpg' == os.path.splitext(outf)[1]:
        decrypt_f()
        gen_pass()
        store()
        crypt_f()
    else:
        gen_pass()
        store()
        crypt_f()
        
    print(color.GREEN+"* Password saved to "+os.path.splitext(outf)[0]+'.gpg')

else:
    parser.error("A required argument is missing")
