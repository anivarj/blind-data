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
import os
import pandas as pd
from tkinter.filedialog import askdirectory


# Choose your raw data location
targetWorkspace = askdirectory(initialdir='~/', message='SELECT YOUR DATA LOCATION') 


# Create the output folder
output = os.path.join(targetWorkspace,'blinded') 
os.mkdir(output)


# Get full paths to original files 
origPaths = [] 

#This section gets a list of files inside targetWorkspace and adds the full paths to origPaths list
for dirpath, dirnames, files in os.walk(targetWorkspace): #walks through targetWorkspace
    files = [f for f in files if not f[0] == '.']         #excludes hidden files in the files list
    dirnames = [d for d in dirnames if not d[0] == '.']   #excludes hidden directories in dirnames list
    
    for file in files:                                    
        origPaths.append(os.path.join(dirpath, file))     #for each file, get the full path to it's location


# Create dataframe
blindedDf = pd.DataFrame(origPaths, columns=["Original Paths"]) #initiate dataFrame with the origPaths list
pd.set_option('display.max_colwidth', None)                     #sets to display the full column width


# ## Create blinded filenames

from random import choice
from string import ascii_uppercase


randomizedPaths = [] #creates empty list for the randomized paths

#This section creates a randomized 5-character filename for every row of the dataFrame and stores it in randomizedPaths
for r in range(0, len(blindedDf)): 
    randomizedPaths.append(os.path.join(output, ''.join(choice(ascii_uppercase) for i in range(5)) + ".tif")) #makes a full path for the randomized name in the output folder

blindedDf['Randomized Paths'] = pd.DataFrame(randomizedPaths) #appends the list of randomized paths to the current DataFrame


# ## Blind the data

newList = list(zip(blindedDf['Original Paths'], blindedDf['Randomized Paths'])) #zipping the two columns from the dataFrame into a list of tuples 

from shutil import copyfile

#for each tuple pair, copy the original file to the randomized path
for orig, randomized in newList:
    copyfile(orig, randomized)


# ## Export the key

csvPath = os.path.join(output, 'blinded-key.csv') #create a path for the exported dataframe

blindedDf.to_csv(csvPath, index=False) #export the dataframe as csv

