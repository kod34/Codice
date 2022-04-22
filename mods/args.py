import argparse
from mods.colors import *
import sys

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')

requiredNamed.add_argument("-c", "--crypt", dest="crypt", help="Encryption algorithm")
requiredNamed.add_argument("-a", "--app", dest="app", help="Resitration app Name")
requiredNamed.add_argument("-u", "--user", dest="user", help="Username associated with the generated password")
requiredNamed.add_argument("-l", "--len", dest="len", help="Generated password length")
requiredNamed.add_argument("-o", "--out", dest="out", help="Output file")


args = parser.parse_args()

# Args initiate
crypt = args.crypt
user = args.user
plen = args.len
outf = args.out
app = args.app
