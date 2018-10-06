import re
import time
import os
import sys

time.sleep(0.5)
print('\33[34m'"""
=======================================
        PROGRAMMED BY ABDXSLAYER
=======================================""")
time.sleep(1)
os.system('clear')
path = raw_input("Enter File Path : ")
os.system('clear')
fp = open(path)
with open(path) as fp:  
   line = fp.readline()
   for i, line in enumerate(fp):
	addressToVerify = line
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
	if match == None:
		print "%s%s%s"%('\33[31m',line,'IS NOT VALID\n')
	if match != None:
		print "%s%s%s"%('\33[32m',line,'IS VALID\n')
