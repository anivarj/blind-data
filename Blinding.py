#!/usr/bin/env python
# coding: utf-8

'''
Author:Ani Michaud (amichaud3@wisc.edu)

Description:
This script should take a folder of .tif files and blind the data by creating a unique, 5-letter code for the file name and renaming the files. 
This script assumes you have python3 installed. The order of the script is as follows:
* Ask the user where their data is stored (targetWorkspace). It can be in individual sub-folders or just copied into one parent folder
* Create an output directory called 'blinded'. 
* Make a list of all the files in the targetWorkspace, and import them into a pandas DataFrame
* Create a 5-letter random code-name (ending in .tif) for each file path in the DataFrame
* Copies the original file to the output 'blinded' folder and renames it to the blinded code-name
* Creates a key .csv file for later unblinding
'''

# Import modules and shit
import os, sys
import pandas as pd
from tkinter.filedialog import askdirectory
from random import choice
from string import ascii_uppercase
from shutil import copyfile, rmtree

# Choose your raw data location
targetWorkspace = askdirectory(initialdir='~/', message='SELECT YOUR DATA LOCATION') 

# Create the output folder called 'blinded'
output = os.path.join(targetWorkspace,'blinded')

if os.path.exists(output):
    rmtree(output)

os.mkdir(output) 

'''This section gets a list of files inside targetWorkspace and adds the full paths to origPaths list'''

origPaths = [] #future list of paths to all original files
filenames = [] #future list of file names

for dirpath, dirnames, files in os.walk(targetWorkspace): #walks through targetWorkspace
    files = [f for f in files if not f[0] == '.']         #excludes hidden files in the files list
    dirnames[:] = [d for d in dirnames if not d[0] == '.']   #excludes hidden directories in dirnames list
    
    for file in files:                                    
        filenames.append(file)                            #append each file name to the filenames list
        origPaths.append(os.path.join(dirpath, file))     #for each file, get the full path to it's location

blindedDf = pd.DataFrame(origPaths, columns=["Original Paths"]) #initiate dataFrame with the origPaths list
blindedDf['Original Names'] = pd.DataFrame(filenames)           #add the original filenames list as a new col


'''This section creates a randomized 5-character filename for every row of the dataFrame and stores it in randomizedPaths'''

randomizedPaths = [] #creates empty list for the randomized paths
randomizedNames = [] #creates empty list for randomized names

for r in range(0, len(blindedDf)): 
    randomName = ''.join(choice(ascii_uppercase) for i in range(5)) + ".tif" #creates randomized file name
    randomizedPaths.append(os.path.join(output, randomName))                 #makes a full path for the randomized name in the output folder
    randomizedNames.append(randomName)                                       #adds the randomized name to randomNames list

data = zip(origPaths, filenames, randomizedPaths, randomizedNames) #zip the data lists together into a tuple
blindedDf = pd.DataFrame(data, columns=["Original Paths", "Original Names", "Randomized Paths", "Randomized Names"]) #initiate dataFrame with the data


'''Blind the data and export key'''
blindedDf.apply(lambda row: copyfile(row['Original Paths'], row['Randomized Paths']), axis = 1) # applies the copyfile function to original paths and randomize paths columns over every row
csvPath = os.path.join(output, 'blinded-key.csv')   #create a path for the exported dataframe
blindedDf.to_csv(csvPath, index=False)              #export the dataframe as csv

