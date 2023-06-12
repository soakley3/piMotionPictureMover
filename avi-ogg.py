# avi-ogg.py
#
# lucas oakley
# This finds the avi files, then uses avconv to convert to ogg theora.
#    This makes them playable through html5 and therefore compatible with 
#    both mobile and desktop sites
#


import os
import shutil

# path for jpeg and avi files
path = "/Users/lucas/camshots/t2/2017/06/11/movies"

def discoverFiles():
    print("Hello")
    files = os.listdir(path)
    videos = []
    for file in files:
        if (os.path.isfile(path+"/"+file)):
            fileType = (file.split(".")[1])
            if fileType == "avi":
                videos.append(file)
    #print(files[-1].split("."))
    return videos

# conversion function to run in the terminal
# avconv -i *.avi -acodec libvorbis *.ogg
def convertFiles(files):
    for file in files:
        newpathfile = path+"/"+file
        if (not (os.path.exists(path+"/ogg"))):
            os.makedirs(newpath+"/ogg")
        runstring = "avconv -i "+newpathfile + " -acodec libvorbis "+ path+"/ogg/"+file.split(".")[0]+".ogg"
        os.system(runstring)
        
#os.system("touch /Users/lucas/Desktop/ttt1.txt")

convertFiles(discoverFiles())
 
       
        
        
        
        
        
        
        
        
        
