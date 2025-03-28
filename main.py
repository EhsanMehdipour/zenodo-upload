#!/usr/bin/env python3
import os
from zenodoupload import ZenodoUpload

def main():
    
    # read the access token from the environment variable
    ACCESS_TOKEN = os.getenv("ZENODO_TOKEN")

    # Check if the access token is loaded.
    if not ACCESS_TOKEN:
        raise ValueError("ZENODO_TOKEN environment variable not provided")

    # Get the information of Zenodo repository.
    # !!! Change DOI_ID.!!!
    my_zenodo = ZenodoUpload(ACCESS_TOKEN=ACCESS_TOKEN, DOI_ID=11111111)
    print(my_zenodo)
    
    # Create the connection with the Zenodo repo and recieve the metadata.
    my_zenodo.connect()
    
    # Upload all the files in the list. 
    # !!! Change filepaths. !!!
    filenames = ['/path/to/the/file1','/path/to/the/file2']
    for filename in filenames:
        my_zenodo.upload_file(filename)

if __name__ == "__main__":
    main()