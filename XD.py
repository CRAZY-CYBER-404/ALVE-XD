import os

from platform import architecture

if architecture()[0]=='64bit':os.system('git pull;chmod +x ALVE;./ALVE')

#elif architecture()[0]=='32bit':os.system('git pull;chmod +x Sefat;./Sefat')

else:exit('\33[1;31m\ Sorry unknown device not support ')
