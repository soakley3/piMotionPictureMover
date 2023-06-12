# fileMover.py
#
# lucas oakley
# This is to move the avi and jpeg files to a directory with 
#     the proper date stamps
#


import os
import shutil

# path for jpeg and avi files
path = "/Users/lucas/camshots/t2"

# returns (videos[], photos[])
def discoverFiles():
    print("Hello")
    files = os.listdir(path)
    videos = []
    photos = []
    for file in files:
        if (os.path.isfile(path+"/"+file)):
            fileType = (file.split(".")[1])
            if fileType == "avi":
                videos.append(file)
            if fileType == "jpg":
                photos.append(file)
    #print(files[-1].split("."))
    return (videos, photos)

# split at the -,
# 01-20170612144305
def parseDate(file):
    # either (file num, date) or (file num, date, useless)
    infoTuple = file.split("-")
    year = infoTuple[1][0:4]
    month = infoTuple[1][4:6]
    day = infoTuple[1][6:8]
    return (year, month, day)

# split at the .
# 01-20170612144305   .avi
def parseDirsAttr(files):
    dirs = []
    for file in files:
        #print("1: "+file)
        #print(file.split(".")[0])
        #print("1.5: ")
        fileDate = parseDate(file.split(".")[0])
        #print()
        #print("2: "+fileDate)
        #print(fileDate)
        dirs.append(fileDate)
        #print("3: ", dirs)
    # list of (tuple year month day)
    # This removes duplicates, converts to a list of tuples
    dirs = list(set(dirs))
    return dirs

# List of tuples is then run through, and the directories are created
def createDirs(attrs):
    for attr in attrs: # add year to path, month, day
        newpath = path+"/"+attr[0]+ "/"+attr[1]+"/"+attr[2]
        if (not (os.path.exists(newpath))):
            os.makedirs(newpath+"/movies")
            os.makedirs(newpath+"/photos")
            
def moveFiles(files):
    # move the avi and jpg files to their respectively correct directories
    # based on the date in the file name
    dateList = parseDirsAttr(files)
    createDirs(dateList)
    for file in files:
        date = parseDate(file)
        type = ""
        if (file.split(".")[1] == "avi"):
            type = "movies"
        else:
            type = "photos"
        
        newpath = path+"/"+date[0]+ "/"+date[1]+"/"+date[2]+"/"+type+"/" +file
        shutil.move(path+"/"+file, newpath)
    


# Start main 
print("Starting...")
flz = discoverFiles()
print("movies: ", flz[0])
print("photos: ", flz[1])
print("Moving photos...")
moveFiles(flz[1])
print("Moving videos...")
moveFiles(flz[0])
print("Complete.")




