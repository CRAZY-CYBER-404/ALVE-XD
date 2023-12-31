import os, platform, time, sys

try:

import requests

except:

os.system('pip install requests')

os.system('git pull --quiet 2>/dev/null')

bit = platform.architecture()[0]

if bit == '64bit':

print('\3[0;97m[•] \3[1;32mCONGRATULATIONS 64BIT SUCCESS')

import ALVE

elif bit == '32bit':os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD?raw=true -o ALVE32')

print('\3[0;97m[•] \3[1;32mCONGRATULATIONS 32BIT SUCCESS')

import ALVE32



