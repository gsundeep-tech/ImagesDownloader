import downloader
import unittest 
import pandas as pd
from unittest import mock

class TestDownloader(unittest.TestCase): 
    def setUp(self):
        self.verbose = False
    
    def test_checkFileType(self):  
        result = downloader.checkFileType("data.txt", self.verbose)       
        self.assertEqual(result, True)
        with self.assertRaises(SystemExit) as cm:
            downloader.checkFileType("data.csv", self.verbose)
        self.assertEqual(cm.exception.code, 1)
    
    @mock.patch('downloader.downloadImage', return_value=True)
    def test_downloadContent(self, mock_info):
        numberOfWorkers = 2
        data = pd.DataFrame(['http://website.com/1.jpg','http://website.com/2.jpg'])
        baseSaveLocation = "./"
        downloader.downloadContent(numberOfWorkers, data, baseSaveLocation, self.verbose)

    @mock.patch('downloader.downloadImage', return_value=None)
    def test_downloadImage(self, mock_info):
        file = "1.jpg"
        link = "http://www.website.com/1.jpg"
        self.assertEqual(downloader.downloadImage(file, link, self.verbose), None)

    @mock.patch('downloader.checkFileType', return_value=True)
    def test_readFileContents(self, mock_info):
        downloader.readFileContents("./datasets/test_data.txt", self.verbose)
  
if __name__ == '__main__': 
    unittest.main() 