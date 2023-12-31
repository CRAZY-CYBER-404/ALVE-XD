#coding=utf-8
import os, sys, platform
os.system('rm -rf ALVE-XD')
os.system('git pull')
try:
    if sys.argv[1]=='ALVE-XD':
        os.system('rm -rf ALVE-XD')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ALVE-XD'):
        os.system('curl -L https://github.com/CRAZY-CYBER-404/ALVE-XD/main/ALVE-XD?raw=true -o ALVE')
        os.system('chmod 777 ALVE;./ALVE)
    else:
        os.system('chmod 777 ALVE;./ALVE')
