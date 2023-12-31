import os, platform, time, sys
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':import RINKU64
elif bit == '32bit':import RINKU32

