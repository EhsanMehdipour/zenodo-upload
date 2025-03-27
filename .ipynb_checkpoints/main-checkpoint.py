#!/usr/bin/env python3
import os
from zenodoupload import ZenodoUpload

def main():
    ACCESS_TOKEN = os.getenv("ZENODO_TOKEN")

    if not ACCESS_TOKEN:
        raise ValueError("ZENODO_TOKEN environment variable not provided")

    my_zenodo = ZenodoUpload(ACCESS_TOKEN=ACCESS_TOKEN, DOI_ID=11111111)

    print(my_zenodo)
    my_zenodo.connect()
    my_zenodo.upload_file('/path/to/the/file')

if __name__ == "__main__":
    main()