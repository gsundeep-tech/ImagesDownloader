# ImagesDownloader

downloader.py is a python program for downloading the bulk images from a given text file into a specific folder. Program uses the multi threading to speed up the download process

This project is hosted at: [https://github.com/gsundeep-tech/ImagesDownloader](https://github.com/gsundeep-tech/ImagesDownloader).

**Requires:**  

- [Python 3.x](https://www.python.org/downloads/)
- [argparse](https://pypi.python.org/pypi/argparse)

## Usage

      python downloader.py --file <dataset_location> --verbose <True/False> \
                           --threads <Number_Of_Threads> --save <save_location>
      
      Example: python downloader.py --file ./datasets/sample.txt --verbose True --threads 7 --save ./images
      
      Running the program only with required arguments: python downloader.py --file ./datasets/sample.txt

<pre>
[Required] -f or --file   : argument, provides the location of the input dataset
[Optional] -v or --verbose: verbosity of the program. 
                               Default value: False
                               Possible Values: True/False 
[Optional] -t or --threads: Number of threads 
                               Default value: 5
[Optional] -s or --save   : save location for downloaded images 
                               Default value: ./images
</pre>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
