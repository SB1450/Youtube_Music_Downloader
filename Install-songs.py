from pytube import YouTube
import sys, os
import requests

##########################    Functions    ########################## 

# Guidance Function
def usage():
    print("\033[1mUsage: Install-songs.py <text_file>\033[0m")
    return exit()

## Function to Install the track/song
def Youtube_install_mp3(url, file_arg=False):
    if not file_arg:
        yt = YouTube(url)
    else:
        yt = YouTube(url)
    print("Installing...")
    video = yt.streams.filter(only_audio=True).first()
    if not os.path.exists(f"{home}/Music/songs"): os.makedirs(f"{home}/Music/songs")
    destination = f"{home}/Music/songs"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")

## Function to validate the url
def url_validation(url):
    if not (url.startswith("https://www.youtube.com") or url.startswith("https://youtu.be")):
        return False
    url_check = requests.get(f"{url}")
    if "This video isn't available anymore" in url_check.text:
        return False
    return True


##########################    MAIN    ########################## 

## Check if files is exists
home = os.path.expanduser('~')
line_count = 1
## Checks if argument was given
try:
    if os.path.exists(sys.argv[1]):
        file = sys.argv[1]
    else:
        print("Invalid argument!")
        usage()
except IndexError:
    url = str(input("Enter URL of youtube video:\n"))
    if url_validation(url):
        Youtube_install_mp3(url)
    else:
        print("Url Invalid!")
        exit()
    exit()

## Runs over lines in the file
with open(f'{file}') as f:
    lines = [line.rstrip('\n') for line in f]
## Remove all empty lines from list
lines = list(filter(None, lines))

for line in lines:
    ## Checking url validation
    if url_validation(line):
        Youtube_install_mp3(line, file_arg=True)
    else:
        print(f"Line {line_count} url Invalid!")
    line_count+=1
exit()