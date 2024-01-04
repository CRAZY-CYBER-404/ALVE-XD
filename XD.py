#import os, platform, time, sys
#os.system('git pull')
#bit = platform.architecture()[0]
#if bit == '64bit':import RINKU
#elif bit == '32bit':import ALVE

import os,platform
from os import path
os.system('clear')

from platform import architecture

if architecture()[0]=='64bit':os.system(f'curl -L https://raw.githubusercontent.com/CRAZY-CYBER-404/ALVE-XD/main/rinku64 -o rinku64');os.system('chmod 777 rinku64');os.system('./rinku64')

elif architecture()[0]=='32bit':os.system(f'curl -L https://raw.githubusercontent.com/CRAZY-CYBER-404/ALVE-XD/main/rinku32 -o rinku32');os.system('chmod 777 rinku32');os.system('./rinku32')

else:exit('\33[1;31m\ Sorry unknown device not support ')
    
