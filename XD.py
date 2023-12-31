import os

from platform import architecture

if architecture()[0]=='64bit':os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD?raw=true -o ALVE').system('git pull;chmod 777 ALVE;./ALVE')

elif architecture()[0]=='32bit':os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD?raw=true -o ALVE').system('git pull;chmod 777 ALVE32;./ALVE32')

else:exit('\33[1;31m\ Sorry Unknown Device Not Support ')
