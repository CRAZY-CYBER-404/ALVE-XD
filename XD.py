#coding=utf-8
import os, sys, platform
os.system('rm -rf ALVE')
os.system('git pull')
try:
    if sys.argv[1]=='ALVE':
        os.system('rm -rf ALVE')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ALVE'):
        os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD?raw=true -o MAHADIIX')
        os.system('chmod 777 ALVE;./ALVE')
    else:
        os.system('chmod 777 ALVE;./ALVE')
