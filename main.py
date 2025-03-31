#!/usr/bin/env python3
import os
from zenodoupload import ZenodoUpload
from tqdm import tqdm

def main():
    
    # !!! Change DOI_ID.!!!
    DOI_ID=1111111
    # !!! Change filepaths. !!!
    filenames = ['/path/to/the/file1','/path/to/the/file2']
    # read the access token from the environment variable
    ACCESS_TOKEN = os.getenv("ZENODO_TOKEN")

    # Check if the access token is loaded.
    if not ACCESS_TOKEN:
        raise ValueError("ZENODO_TOKEN environment variable not provided")

    # Get the information of Zenodo repository.
    my_zenodo = ZenodoUpload(ACCESS_TOKEN=ACCESS_TOKEN, DOI_ID=DOI_ID)
    print(my_zenodo)
    
    # Create the connection with the Zenodo repo and recieve the metadata.
    my_zenodo.connect()
    
    # Upload all the files in the list. 
    for filename in tqdm(filenames):
        my_zenodo.upload_file(filename)

if __name__ == "__main__":
    main()