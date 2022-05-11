import subprocess
import os
import random
import string
from mods.colors import *
from mods.args import *
        
def decrypt_f():
    print(color.BLUE+"Decrypting "+color.YELLOW+outf+"..."+color.END)
    try:
        subprocess.call(['gpgconf', '--kill', 'gpg-agent'])
        subprocess.check_output(['gpg', outf], stderr=subprocess.STDOUT)
        print(color.GREEN+"[+] Decryption successful"+color.END)
    except subprocess.CalledProcessError:
        sys.exit(color.RED+"\n[-] Decryption failed..."+color.END)
    
def gen_pass():
    global password
    print(color.BLUE+"Generating random password of size "+color.YELLOW+plen+"..."+color.END)
    password = ''
    source = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pass_list = list(source)
    random.SystemRandom().shuffle(pass_list)
    
    for i in range(int(plen)):
        password += random.choice(pass_list)
    print(color.GREEN+"[+] Password generated: "+color.YELLOW+password+color.END)

def store():
    print(color.BLUE+"Storing data in "+color.YELLOW+os.path.splitext(outf)[0]+"..."+color.END)
    new_line = "\t-"+(str(app)).upper()+':\n'+str(user)+':'+str(password)
    with open(os.path.splitext(outf)[0], 'a') as o:
        o.write(new_line+'\n')
        print(color.GREEN+"[+] Password has been stored"+color.END)

def crypt_f():
    print(color.BLUE+"Encrypting "+color.YELLOW+os.path.splitext(outf)[0]+"..."+color.END)
    try:
        subprocess.check_output(['gpg', '-c', '-crypt-algo='+str(crypt), os.path.splitext(outf)[0]],
    stderr=subprocess.STDOUT)
        print(color.GREEN+"[+] Encryption successful"+color.END)
    except subprocess.CalledProcessError:
        sys.exit(color.RED+"\n[-] Encryption failed..."+color.END)
    try:
        os.remove(os.path.splitext(outf)[0])
    except:
        pass
