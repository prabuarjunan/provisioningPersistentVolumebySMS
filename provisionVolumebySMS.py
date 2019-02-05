from botocore.vendored import requests
import logging
import json



#logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

CVAPI_BASEURL="https://cds-aws-bundles.netapp.com:8080/v1"
CVAPI_APIKEY="Enter your keys here"
CVAPI_SECRETKEY="Enter your keys here"


#Headers
HEADERS = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
    }

getfilesystemDetailsHeaders = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
}


filesystemURL = CVAPI_BASEURL + "/FileSystems"
filesystemCreateURL = CVAPI_BASEURL

def lambda_handler(event, context):
    payload = {
        "name": "AutomatedVolume",
        "creationToken": "ACV7",
        "region": "us-east-1",
        "serviceLevel": "basic",
        "quotaInBytes": 1000000000000
    }
    postfileSystems = requests.post(filesystemURL, data=json.dumps(payload), headers=HEADERS)
    print("FileSystem Created", filesystemURL, postfileSystems.status_code, postfileSystems.json())
    if postfileSystems.status_code == 202:
        print ("Task success")
        return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>Volume create success</Message></Response>'