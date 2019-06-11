# importing the necessary libraries
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlretrieve
from datetime import datetime
from os.path import isfile, exists
import pandas as pd
import sys
import os
import time

not_downloaded = []

def downloadImage(file, link, verbose):
    """
    description: downloads the image from the given link
    inputs: file - file name to saved as
            link - image url
    """
    try:
        urlretrieve(link, file)
        if verbose:
            print("[Info] Image downloaded from url: ", link)
    except Exception as ex:
        if verbose:
            print("[Error] ", ex, "Not able to download image from ", link)
        not_downloaded.append(link)

def downloadContent(numberOfWorkers, data, baseSaveLocation, verbose):
    """
    description: Adds the url's to threads if the image is not downloaded
    input: numberOfWorkers - Number of threads, by default threads count is 5
           data - URL's dataframe
           baseSaveLocation - location to save the downloaded images, by default base location is ./images 
    """
    # creating the save directory if not exists 
    if not exists(baseSaveLocation):
        os.makedirs(baseSaveLocation)

    # starting the threads
    with ThreadPoolExecutor(max_workers=numberOfWorkers) as executor:
        for _, row in data.iterrows():
            link = row[0]
            fileName = link.split("/")[-1]
            file = baseSaveLocation + "/" + fileName
            if not isfile(file):
                executor.submit(downloadImage, file, link, verbose)

def checkFileType(fileLocation, verbose):
    """
    description: Checks if the file is a text file or not
    input: file location path
    returns: True if it is a valid text file otherwise exits the program 
    """
    if verbose:
        print("[INFO] Checking file type")
    fileNameInfo = fileLocation.split('.')
    if len(fileNameInfo) > 1 and fileNameInfo[-1] == "txt":
        return True
    print("[Error] Enter valid text file")
    sys.exit(1)

def readFileContents(fileLocation, verbose):
    """
    description: Reads the data from the file and removes if any null rows are present
    input: file location path
    returns: data in the file
    """
    try:
        # Restricting the inputs to CSV
        validTextFile = checkFileType(fileLocation, verbose)
        if (validTextFile):
            if verbose:
                print("[Info] Reading file contents")
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

    parser.add_argument('-s', '--save', dest='saveLocation', 
                        help='Save folder Location', default='./images')

    parser.add_argument('-t', '--threads', dest='threadsCount', help="Number of threads", default=5, type=int)

    parser.add_argument('-v', '--verbose', dest='verbose', help="Verbose", default=False, type=bool)

    args = parser.parse_args()
    
    start_time = time.time()
    print("[Info] program started...")
    # Reading the data from the file
    data = readFileContents(args.fileLocation, args.verbose)
    
    # Only download the content if there is any data available in file
    if data.size > 0:
        downloadContent(args.threadsCount, data, args.saveLocation, args.verbose)
    
    # creating a log file if any images are not downloaded
    if len(not_downloaded) > 0:
        fileName = datetime.now().strftime('notDownloaded_%H_%M_%d_%m_%Y.txt')
        with open(fileName, 'w') as f:
            f.writelines(["%s\n" % item  for item in not_downloaded])
    
    # calculating the total duration in seconds
    duration = time.time() - start_time

    # Printing the meta information to the user
    if args.verbose:
        print("_______________________________________________________________________")
        print("[Info] Number of URL's parsed: ", data.size)
        print("[Info] Number of Images not able to download: ", len(not_downloaded))
        print("[Info] time taken for executing process: ", str(duration), " seconds")