import os, shutil
import requests
import mechanize
import pandas as pd
import csv
from time import sleep
import datetime

def updateCSV():
    # Get the current working directory
    folder = os.getcwd()
    folder = os.path.join(folder, "Data/DataCSVs")
    # Delete all existing CSVs
    d = datetime.datetime.today()
    day = str(d.day) + "-" + str(d.month) + "-" + str(d.day)
    print("Deleting outdated CSVs")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if file_path.find(day) == -1:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    if len(os.listdir(folder)) == 0:
        # Make a Browser (think of this as chrome or firefox etc)
        br = mechanize.Browser()

        #visit http://stockrt.github.com/p/emulating-a-browser-in-python-with-mechanize/
        #for more ways to set up your br browser object e.g. so it look like mozilla
        #and if you need to fill out forms with passwords.

        # Open your site
        br.open("https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases")

        filetypes = [".csv"] # you will need to do some kind of pattern matching on your files
        myfiles = []
        for l in br.links(): # you can also iterate through br.forms() to print forms on the page!
            for t in filetypes:
                if t in str(l): # check if this link has the file extension we want (you may choose to use reg expressions or something)
                    myfiles.append(l)

        # for f in myfiles:
        #     print(f)


        def downloadlink(l):
            if l.text != "Validate with Data Check":
                folder = os.getcwd()
                folder = os.path.join(folder, "Data/DataCSVs")
                text = list(l.text)
                # Find out where the .csv starts
                ind = text.index(".")
                # Remove the download and end part
                text = text[9:ind + 4]
                fileName = ""
                for c in text:
                    fileName += c
                saveName = fileName[:-4] + day + ".csv"
                print(saveName)

                baseUrl = "https://data.humdata.org/"
                with open(os.path.join(folder, fileName), "w", newline="") as outputFile:  # perhaps you should open in a better way & ensure that file doesn't already exist.
                    br.click_link(l)
                    location = list(str(br.retrieve(baseUrl + l.url)).split(","))[0][2:-1]
                    shutil.move(location, os.path.join(folder, fileName))
                    os.rename(os.path.join(folder, fileName), os.path.join(folder, saveName))
                    print(os.path.join(folder, saveName), "was created")


        for l in myfiles:
            sleep(1) # throttle so you dont hammer the site
            downloadlink(l)
        
# Debug
if __name__ == "__main__":
    updateCSV()

