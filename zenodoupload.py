import os
import requests

class ZenodoUpload():
    def __init__(self,ACCESS_TOKEN, DOI_ID):
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.DOI_ID = DOI_ID
        self.check()
        
    def check(self):
        if not self.ACCESS_TOKEN:
            raise ValueError("ACCESS TOKEN not provided")
        if not self.DOI_ID:
            raise ValueError("DOI ID of Zenodo repository is not provided")
        if not isinstance(self.DOI_ID, int):
            raise ValueError("DOI ID of Zenodo repository should be an integer.")
        
    def __str__(self):
        return f'Zenodo API address: https://zenodo.org/api/deposit/depositions/{self.DOI_ID}'
    
    def connect(self):
        r = requests.get(f'https://zenodo.org/api/deposit/depositions/{self.DOI_ID}',
                  params={'access_token': self.ACCESS_TOKEN})
        print(r)
        self.requests = r
        
        self.json = r.json()
        
    def upload_file(self, filepath):
        filename = os.path.basename(filepath)
        
        bucket_url = self.json["links"]['bucket']
        
        with open(filepath, "rb") as fp:
            r = requests.put(
                "%s/%s" % (bucket_url, filename),
                data=fp,
                params={'access_token': self.ACCESS_TOKEN},
            )
        print(f"Upload successful: {filepath}")