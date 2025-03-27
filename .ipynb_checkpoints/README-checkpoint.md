# Upload files to Zenodo using API
Upload files directly to the Zenodo repository using the API

## Requirements

**Token:** create a token in Zenodo --> Profile --> Application --> Personal access tokens --> New Token.

Save this token as an environment variable called "ZENODO_TOKEN" in the system to be accessible by os.getenv("ZENODO_TOKEN").

**DOI_ID:** Create a repository in Zenodo and reserve a DOI. Use the DOI ID in the code as DOI_ID.
