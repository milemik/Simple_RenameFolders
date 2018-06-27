#!/usr/bin/python3

import os
import random
from glob import glob

pwd = os.getcwd()

list_dir = glob('{}/*/'.format(pwd))

for x in list_dir:
    num = random.randint(0,100)
    os.rename(x,'{}/Folder{}'.format(pwd,num))

print("Rename COMPLITED!")


