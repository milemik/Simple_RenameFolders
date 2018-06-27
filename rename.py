#!/usr/bin/python3

import os
import random
from glob import glob
#get the path to curent working dir
pwd = os.getcwd()
#find all sub dir in that path
list_dir = glob('{}/*/'.format(pwd))
# For every dir path in list_dir
for x in list_dir:
    #give random number 0 - 100
    num = random.randint(0,100)
    #rename the dir to Folder+randnum EXAMPLE: Folder66
    os.rename(x,'{}/Folder{}'.format(pwd,num))
#after rename all folders print "Rename COMPLITED"
print("Rename COMPLITED!")


