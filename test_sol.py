#!/usr/bin/env python2.7
import random
import os
import glob
import datetime
import pdb
import unittest
from filesearch_sol import filesearch, count_keyword_files, main

# Part 1
# creates random number of files (no more than 30) in the root dir with random number of keywords
basename = "filesearch_sol"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")

root_dir = ""
os.chdir("")
keyword1 = ""
keyword2 = ""
keyword3 = ""

# keyword1
random_files = random.randrange(1, 10)
print("Amount of files with keyword1 created: ", random_files)
i = 1
while i <= random_files:
    num = str(i)
    filename = "_".join([basename + "1", num, suffix])
    with open(filename, 'U') as f:
        random_words = random.randrange(1, 20)
        q = 1
        while q <= random_words:
            f.write(keyword1)
            q += 1
    i += 1
print("Files with keywords have been created in root dir")
input("Press Enter to continue...")
print('\n')

#next
Keywords_list = ['^[a-zA-Z]+_TESTResult.*', 'abc', 'abcd']
Amount_files = [0, 0, 0]
print("List of files in the root dir:")
for file in os.listdir(root_dir):
    print(file)
    with open(file, 'r') as f:
        data = f.readlines()
        for line in data:
            words = line.split(' ')
        for y in words:
            if y == "^[a-zA-Z]+_TESTResult.*":
                Amount_files[0] += 1
                break
            elif y == "abc":
                Amount_files[1] += 1
                break
            else:
                if y == "abcd":
                    Amount_files[2] += 1
                    break
print("Keyword 1 (^[a-zA-Z]+_TESTResult.*) in ", Amount_files[0], " files present")
print("Keyword 2 (abc) in ", Amount_files[1], " files present")
print("Keyword 3 (abcd) in ", Amount_files[2], " files present")
print('\n')
input("Press Enter to clear C:\Test\Files directory...")
files = glob.glob('C:/Test/Files/*')
for f in files:
    os.remove(f)
input("All files in work directory have been deleted. Press Enter to exit...")
