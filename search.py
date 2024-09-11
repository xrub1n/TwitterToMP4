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
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if(isMP4(line)):
                return findLink(line, previousLine)
            previousLine = line



def isMP4(line):    #checks if the string ".mp4" is contained in the line.
    return re.findall('.mp4',line)

def findLink(line, previousLine):
    index = len(line)
    while(index >= 3):
        index -= 1
        if(line[index] == "4" and line[index-1] == "p" and line[index-2] == "m" and line[index-3] == "."):
            return getLink(line,index,"",previousLine)
                    
                    
        
def getLink(line,index,link="",previousLine=""):
    while(line[index] != '"'):
        link = line[index] + link
        index -= 1
        if(index < 0):
            return getLink(previousLine,len(previousLine)-1,link)
    return link

def main():
    filename = "data/data.txt"
    
    link = parseFile(filename)
    print()
    print("\n The link to the mp4 provided is: \n" + link)

main()