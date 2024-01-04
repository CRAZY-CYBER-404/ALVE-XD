#import os, platform, time, sys
#os.system('git pull')
#bit = platform.architecture()[0]
#if bit == '64bit':import RINKU
#elif bit == '32bit':import ALVE

import os,platform
from os import path
os.system('clear')
print('\n\n\n\033[0;37m installing setup....\n')
chk = platform.architecture()[0]
if '64bit' in chk:
    if path.isfile("rinku64"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/CRAZY-CYBER-404/ALVE-XD/main/rinku64 -o rinku64');os.system('chmod 777 rinku64');os.system('./rinku64')
if '32bit' in chk:
    if path.isfile("rinku32"):
        pass
    else:
        os.system(f'curl -L https://raw.githubusercontent.com/CRAZY-CYBER-404/ALVE-XD/main/rinku32 -o rinku32');os.system('chmod 777 rinku32');os.system('./rinku32')
else:
    exit('\n\n\n\033[1;31m Sorry, Your Device Not Support')
