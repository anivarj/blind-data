# Getting Started
## Description:
* This script should take a folder of .tif files and blind the data by creating a unique, 5-letter code for the file name and renaming the files. 
* This script assumes you have python3 installed. 
* This script needs the pandas package. If you do not have this package, please install via pip or conda: <br><br>
> <code>conda install pandas</code>

# Script rundown
## Import modules


```python
import os
import pandas as pd
from tkinter.filedialog import askdirectory
from random import choice
from string import ascii_uppercase
from shutil import copyfile
```

## Choose your raw data location
Can be in individual sub-folders or just copied into one parent folder


```python
targetWorkspace = askdirectory(initialdir='~/', message='SELECT YOUR DATA LOCATION') 
```

## Create the output folder called 'blinded'


```python
output = os.path.join(targetWorkspace,'blinded') 
os.mkdir(output)
```

## Get full paths to original files and make a dataframe


```python
origPaths = [] #future list of paths to all original files
filenames = [] #future list of file names
```

### Make a list of all the files in the targetWorkspace


```python
#This section gets a list of files inside targetWorkspace and adds the full paths to origPaths list
for dirpath, dirnames, files in os.walk(targetWorkspace): #walks through targetWorkspace
    files = [f for f in files if not f[0] == '.']         #excludes hidden files in the files list
    dirnames = [d for d in dirnames if not d[0] == '.']   #excludes hidden directories in dirnames list
    
    for file in files:
        filenames.append(file)                            #append each file name to the filenames list
        origPaths.append(os.path.join(dirpath, file))     #for each file, get the full path to it's location

```

### Create dataframe


```python
blindedDf = pd.DataFrame(origPaths, columns=["Original Paths"]) #initiate dataFrame with the origPaths list
blindedDf['Original Names'] = pd.DataFrame(filenames)           #add the original filenames list as a new col
pd.set_option('display.max_colwidth', None)                     #sets to display the full column width
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Original Paths</th>
      <th>Original Names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/mri-stack.tif</td>
      <td>mri-stack.tif</td>
    </tr>
    <tr>
      <th>1</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/flybrain.tif</td>
      <td>flybrain.tif</td>
    </tr>
    <tr>
      <th>2</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blobs.tif</td>
      <td>blobs.tif</td>
    </tr>
    <tr>
      <th>3</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/boats.tif</td>
      <td>boats.tif</td>
    </tr>
    <tr>
      <th>4</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/clown.tif</td>
      <td>clown.tif</td>
    </tr>
  </tbody>
</table>
</div>


## Create blinded filenames


```python
randomizedPaths = [] #creates empty list for the randomized paths
randomizedNames = [] #creates empty list for randomized names
```

### Create a 5-letter random code-name for each file


```python
for r in range(0, len(blindedDf)):
    randomName = ''.join(choice(ascii_uppercase) for i in range(5)) + ".tif" #creates randomized file name
    randomizedPaths.append(os.path.join(output, randomName))                 #makes a full path for the randomized name 
    randomizedNames.append(randomName)                                       #adds the randomized name to randomNames list

blindedDf['Randomized Paths'] = pd.DataFrame(randomizedPaths) #appends the list of randomized paths to the current DataFrame
blindedDf['Randomized Names'] = pd.DataFrame(randomizedNames) #adds a new column for the randomized names
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Original Paths</th>
      <th>Original Names</th>
      <th>Randomized Paths</th>
      <th>Randomized Names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/mri-stack.tif</td>
      <td>mri-stack.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/GDAAX.tif</td>
      <td>GDAAX.tif</td>
    </tr>
    <tr>
      <th>1</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/flybrain.tif</td>
      <td>flybrain.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/HPBGX.tif</td>
      <td>HPBGX.tif</td>
    </tr>
    <tr>
      <th>2</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blobs.tif</td>
      <td>blobs.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/GJBUE.tif</td>
      <td>GJBUE.tif</td>
    </tr>
    <tr>
      <th>3</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/boats.tif</td>
      <td>boats.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/YPYXE.tif</td>
      <td>YPYXE.tif</td>
    </tr>
    <tr>
      <th>4</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/clown.tif</td>
      <td>clown.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/QMCXY.tif</td>
      <td>QMCXY.tif</td>
    </tr>
  </tbody>
</table>
</div>


## Blind the data
### Copy the original file to the output folder and rename it to the blinded code-name


```python
newList = list(zip(blindedDf['Original Paths'], blindedDf['Randomized Paths'])) #zipping the two columns from the dataFrame into a list of tuples 

#for each tuple pair, copy the original file to the randomized path
for orig, randomized in newList:
    copyfile(orig, randomized)
```

## Export the key


```python
csvPath = os.path.join(output, 'blinded-key.csv') #create a path for the exported dataframe
blindedDf.to_csv(csvPath, index=False) #export the dataframe as csv
```
