import os, platform, sys
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '32bit':
import ALVE32

#elif bit == '32bit':os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD?raw=true -o ALVE32')

#print('\3[0;97m[•] \3[1;32mCONGRATULATIONS 32BIT SUCCESS')

#import ALVE32



