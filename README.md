# Youtube Song Dowaloader

## This Youtube Song Dowaloader was build with python 3.10

This is a python script that install track/song from Youtube by url . the script cat get as argument a text file with Url's and install them all one by one. I build this script to save myself time instead of using some questionable sites and run into lot of ads this will install the song/track only by url

### ****Before you run the script you need to install the requirements.txt file**
• Install the requirements.txt file
```
pip install -r requirements.txt
```
<sub>if you have problem with modules check [here](https://www.quora.com/I-used-pip-to-install-a-library-but-when-I-import-it-it-says-Module-Not-Found-Why-is-that)</sub>

============================================================================================================

**Install-songs.py** is a python script that can get one argument:

Text-file - In our case the **songs.txt** file . This file will contain Url's seperated by new line (one url per line).

If no argument is given then the program will ask you to give one url as input and will install it

<sub>The songs.txt file conatin one song for demonstration - ["Alec Benjamin - Let Me Down Slowly"](https://www.youtube.com/watch?v=50VNCymT-Cs)</sub>

The script installs all the url's that were given in the text file and save then in **Home/Music/songs** folder/directory if the directory is not exists it will create it

**Usage:**
1.    **python3 Install-songs.py** - for one url
2.    **python3 Install-songs.py <songs.txt>** - for multiple url's
