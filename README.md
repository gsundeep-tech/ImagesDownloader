# ImagesDownloader

downloader.py is a python program for downloading the images from a given text file.


## Usage

```python
python downloader.py --file ./datasets/sample.txt --verbose True --threads 7 --save ./images

[Required] -f or --file: argument, provides the location of the input dataset
[Optional] -v or --verbose: verbosity of the program. 
                            Default value: False
                            Possible Values: True/False 
[Optional] -t or --threads: Number of threads 
                            Default value: 5
[Optional] -s or --save: save location for downloaded images 
                            Default value: ./images

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
