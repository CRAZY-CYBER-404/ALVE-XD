import os,platform
from os import path
os.system('clear')
os.system('git pull')
from platform import architecture
if architecture()[0]=='64bit':os.system('git clone https://github.com/CRAZY-CYBER-404/ALVE-XD/Pro');os.system('chmod 777 Pro');os.system('./Pro')
if architecture()[0]=='32bit':os.system('git clone https://github.com/CRAZY-CYBER-404/ALVE-XD/Pro1');os.system('chmod 777 Pro1');os.system('./Pro1')
else:exit('\33[1;31m[!] Sorry Your  Device Not Support ')
