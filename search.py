import re

# Author: Joshua Rubin-Garcia
# Function: This program takes in the HTML of a twitter post, and return the link to the included video's mp4.

def opener(filename):
    try:
        file = open(filename)
        file.close
        return True
    except:
        print("File not found: ", filename)
        return False

def parseFile(filename):
    previousLine = ""
    current = ""
    with open(filename) as file:
        for line in file:
            if(isMP4(line)):
                return getLink(line, previousLine)


def isMP4(line):
    if(re.findall('.mp4'), line):
        return True
    else:
        return False

def getLink(line, previousLine):

def main():
    filename = "data/data.txt"
    
    search(filename)
main()