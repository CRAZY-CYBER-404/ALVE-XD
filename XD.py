import os, platform, time, sys
os.system('git pull --quiet 2>/dev/null')

bit = platform.architecture()[0]

if bit == '64bit':import ALVE64
  print('\3[0;97m[•] \3[1;32mCONGRATULATIONS 64BIT SUCCESS')
elif bit == '32bit':import ALVE32
	print('\3[0;97m[•] \3[1;32mCONGRATULATIONS 32BIT SUCCESS')



