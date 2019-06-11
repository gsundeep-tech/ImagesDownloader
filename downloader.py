# importing the necessary libraries
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlretrieve
from os.path import isfile
import pandas as pd
import sys

not_downloaded, log = [], []

def downloadImage(file, link):
    """
    description: downloads the image from the given link
    inputs: file - file name to saved as
            link - image url
    """
    try:
        urlretrieve(link, file)
    except Exception as ex:
        print(ex)
        print(link, " is not downloaded")
        not_downloaded.append(link)

def downloadContent(numberOfWorkers, data, baseSaveLocation):
    """
    description: Adds the url's to threads if the image is not downloaded
    input: numberOfWorkers - Number of threads, by default threads count is 5
           data - URL's dataframe
           baseSaveLocation - location to save the downloaded images, by default base location is ./images 
    """
    with ThreadPoolExecutor(max_workers=numberOfWorkers) as executor:
        for _, row in data.iterrows():
            link = row[0]
            print(link)
            fileName = link.split("/")[-1]
            file = baseSaveLocation + "/" + fileName
            if not isfile(file):
                executor.submit(downloadImage, file, link)

def checkFileType(fileLocation):
    """
    description: Checks if the file is a text file or not
    input: file location path
    returns: True or False  
    """
    fileNameInfo = fileLocation.split('.')
    if len(fileNameInfo) > 1 and fileNameInfo[-1] == "txt":
        return True
    print("Enter valid text file")
    sys.exit()

def readFileContents(fileLocation):
    """
    description: Reads the data from the file and removes if any null rows are present
    input: file location path
    returns: data in the file
    """
    try:
        # Restricting the inputs to CSV
        validTextFile = checkFileType(fileLocation)
        if (validTextFile):
            data = pd.read_csv(fileLocation, header=None)
            data.dropna(inplace=True)
            return data
    except IOError as err:
        print(err)
    
if __name__ == '__main__':

    # Arguments for the program
    parser = ArgumentParser(description="Program to download the images from given txt file")
    
    parser.add_argument('-f', '--file', dest='fileLocation', 
                        help='Input text file location', required=True)

    parser.add_argument('--save', dest='saveLocation', 
                        help='Save folder Location', default='./images')

    parser.add_argument('-t', '--threads', dest='threadsCount', help="Number of threads", default=5, type=int)

    parser.add_argument('-v', '--verbose', dest='verbose', help="Verbose", default=False, type=bool)

    args = parser.parse_args()
    
    # Reading the data from the file
    data = readFileContents(args.fileLocation)
    if data.size > 0:
        downloadContent(args.threadsCount, data, args.saveLocation)
