# Getting Started
## Description:
* This script should take a folder of .tif files and blind the data by creating a unique, 5-letter code for the file name and renaming the files. 
* This script assumes you have python3 installed. 
* This script needs the pandas package. If you do not have this package, please install via pip or conda: <br><br>
```conda install pandas```


# Script rundown
1. Choose your raw data location: can be in individual sub-folders or just copied into one parent folder
2. Creates the output folder called 'blinded'
3. Makes a dataframe of file paths and names
4. Creates a 5-letter random code-name for each file
5. Blinds the data and save to the output location
6. Exports the key


## Example Key

<div>

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
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/FHBSY.tif</td>
      <td>FHBSY.tif</td>
    </tr>
    <tr>
      <th>1</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/flybrain.tif</td>
      <td>flybrain.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/BMQQC.tif</td>
      <td>BMQQC.tif</td>
    </tr>
    <tr>
      <th>2</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blobs.tif</td>
      <td>blobs.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/ZHYSV.tif</td>
      <td>ZHYSV.tif</td>
    </tr>
    <tr>
      <th>3</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/boats.tif</td>
      <td>boats.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/BRPQW.tif</td>
      <td>BRPQW.tif</td>
    </tr>
    <tr>
      <th>4</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/clown.tif</td>
      <td>clown.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/DTMBF.tif</td>
      <td>DTMBF.tif</td>
    </tr>
    <tr>
      <th>5</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/CROHQ.tif</td>
      <td>CROHQ.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/AIOKA.tif</td>
      <td>AIOKA.tif</td>
    </tr>
    <tr>
      <th>6</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/blinded-key.csv</td>
      <td>blinded-key.csv</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/DCGKM.tif</td>
      <td>DCGKM.tif</td>
    </tr>
    <tr>
      <th>7</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/NDUUP.tif</td>
      <td>NDUUP.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/UIMZD.tif</td>
      <td>UIMZD.tif</td>
    </tr>
    <tr>
      <th>8</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/FZHLF.tif</td>
      <td>FZHLF.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/PWQEQ.tif</td>
      <td>PWQEQ.tif</td>
    </tr>
    <tr>
      <th>9</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/VXMSV.tif</td>
      <td>VXMSV.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/JOWSF.tif</td>
      <td>JOWSF.tif</td>
    </tr>
    <tr>
      <th>10</th>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/JOVRH.tif</td>
      <td>JOVRH.tif</td>
      <td>/Users/animichaud/Documents/GitHub/Ani/blind-data/test-data/blinded/SLVGT.tif</td>
      <td>SLVGT.tif</td>
    </tr>
  </tbody>
</table>
</div>

