'''
Created on May 3, 2017
@author: Geetha
'''
import os,re
import matplotlib.pyplot as matplt
import numpy as npy

#search all files in given directory
def SearchKeywordInFile(curr_dir, exp):
    results = {}
    count = 0
    matches=[]
    #list all files directory
    for filename in os.listdir(curr_dir):
        #check to make sure it is a file
        file_path = os.path.join(curr_dir,filename)
        if os.path.isfile(file_path):
            #open file, check for matches
            with open(file_path, 'r') as f:
                regx = re.compile(exp)
                for line in f:
                  matches = regx.findall(line)
                  for match in matches:
                      count += 1

        #store count into array for given subdir
        results[curr_dir] = count
    
    return results[curr_dir]
    
root_dir = input('Enter root directory: ')
keyword = input('Enter keyword to search: ')
output = {}
#recursively walk through all dirs & call FileSearch for each subdir
for root, dirs, files in os.walk(root_dir):
    output[root] = SearchKeywordInFile(root, keyword)
#output array of all the data
print(output)


#output bar graph using matplotlib 
graph = npy.arange(len(output))
matplt.bar(graph, output.values(), align='center', width=0.5)
matplt.xticks(graph, output.keys())
matplt.ylim(0, max(output.values())+2)

matplt.title('Number of Files with Keyword')
matplt.xlabel('Subdirectory Names')
matplt.ylabel('Count Values')
matplt.savefig("resultGraph.png", dpi=100)
matplt.show()
