import os,platform
from os import path
os.system('clear')
os.system('git pull')
from platform import architecture
if architecture()[0]=='64bit':os.system(f'curl -L https://raw.githubusercontent.com/CRAZY-CYBER-404/ALVE-XD/main/Pro -o Pro');os.system('chmod 777 Pro');os.system('./Pro')
else:exit('\33[1;31m[!] Sorry 32bit Device Not Support ')
    
