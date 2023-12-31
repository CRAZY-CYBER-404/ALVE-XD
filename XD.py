#import os, platform, time, sys
#os.system('git pull')
#bit = platform.architecture()[0]
#if bit == '64bit':import ALVE64
#elif bit == '32bit':import ALVE32


import os, platform, time, sys 
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;92mChecking For Update. . . .')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':import ALVE64
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 64BIT USER')
elif bit == '32bit':import ALVE32
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 32BIT USER')


