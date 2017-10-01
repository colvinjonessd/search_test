#!/usr/bin/python2.7
import random
import os
import glob
import datetime
import pdb 

# Part 2
'''script recursively walks the “root_dir” and detects all the files under that dir contains “keywords”
and counts the number of files for that sub dir'''
# Prints list of files in the root dir
Keywords_list = ['^[a-zA-Z]+_TESTResult.*', 'abc', 'abcd']
Amount_files = [0, 0, 0]
print("List of files in the root dir:")
for file in os.listdir('/Users/solo/Documents/Coding Test'):
    print(file)
    with open(file) as f:
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
input("Press Enter to clear ...")
files = glob.glob('/Users/solo/Documents')
for f in files:
    os.remove(f)
input("All files in work directory have been deleted. Press Enter to exit...")




