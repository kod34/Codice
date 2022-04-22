import subprocess
import os
from unicodedata import digit
import random
import string
from mods.colors import *
from mods.args import *
        
def decrypt_f():
    print(color.BLUE+"+ Decrypting "+outf+"..."+color.END)
    cmd = subprocess.run(['gpg', outf], capture_output=True).stdout.decode()
    print(cmd)
    
def gen_pass():
    global password
    password = ''
    source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pass_list = list(source)
    random.SystemRandom().shuffle(pass_list)
    
    for i in range(int(plen)):
        password += random.choice(pass_list)

def store():
    new_line = "\t"+(str(app)).upper()+'\n'+str(user)+':'+str(password)
    with open(os.path.splitext(outf)[0], 'a') as o:
        o.write('\n'+new_line)

def crypt_f():
    print(color.BLUE+"+ Encrypting "+os.path.splitext(outf)[0]+"..."+color.END)
    cmd = subprocess.run(['gpg', '-c', '-crypt-algo='+str(crypt), os.path.splitext(outf)[0]], capture_output=True).stdout.decode()
    os.remove(os.path.splitext(outf)[0])
    print(cmd)


