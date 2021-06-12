import logging
import time
import requests
import json
import base64
import boto3
from generate_token import *

base_url = 'https://api-euw1.rms.com/riskmodeler/v1'

# Generate Token
get_token()

# Create Bucket
response_body = requests.post(url=f'{base_url}/storage', headers=headers)
print("delay starts")
print(response_body.headers)
time.sleep(5)
print("delay ends")
bucketId = response_body.headers["Location"].split("/")[-1]
print(bucketId)
# bucketId = 9701

# Create Bucket and Credentials for Account file
body = {
    "fileName": "accexp.txt",
    "fileSize": 0,
    "fileType": "account",
    "fileInputType": "MRI"
}

response_body = requests.post(url=f'{base_url}/storage/{bucketId}/path', headers=headers, json=body)
print(response_body.text)

accessKeyId = base64.b64decode(json.loads(response_body.text)["accessKeyId"]).decode("utf-8")
print(accessKeyId)
secretAccessKey = base64.b64decode(json.loads(response_body.text)["secretAccessKey"]).decode("utf-8")
print(secretAccessKey)
sessionToken = base64.b64decode(json.loads(response_body.text)["sessionToken"]).decode("utf-8")
print(sessionToken)
s3Path = base64.b64decode(json.loads(response_body.text)["s3Path"]).decode("utf-8")
print(s3Path)
s3Region = base64.b64decode(json.loads(response_body.text)["s3Region"]).decode("utf-8")
print(s3Region)
bucketName = s3Path.split("/")[0]
print(bucketName)
s3Path = s3Path[s3Path.index("/") + 1:]
print(s3Path)
fileName = body["fileName"]
print(fileName)
fileId = [response_body.headers["Location"].split("/")[-1]]
print(fileId)

#  UPLOAD ACCOUNT FILE

s3 = boto3.client(
    's3',
    region_name=s3Region,
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretAccessKey,
    aws_session_token=sessionToken
)
key = s3Path + '/' + fileId[0] + '-' + fileName
print(key)

# acc_file = '.\\import_files\\accexp.txt'
# file_upload = s3.upload_file(acc_file, bucketName, key)

# AWS implementation of the ProcessPercentage
import os
import sys
import threading


class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


print("\n\nUPLOADING ACCOUNT FILE\n\n")

with open('.\\import_files\\accexp.txt', 'r') as f:
    content = f.read()
print(response_body)
response_body = s3.put_object(Bucket=bucketName, Key=key, Body=content)


# acc_file = '.\\import_files\\accexp.txt'
# with open(acc_file, "rb") as f:
#     s3.upload_file(f, bucketName, key)
# , Callback=ProgressPercentage(f)
# One more way to provide chunks
# import os
# import progressbar
#
# acc_file = '.\\import_files\\accexp.txt'
# statinfo = os.stat(acc_file)
# up_progress = progressbar.progressbar.ProgressBar(maxval=statinfo.st_size)
# up_progress.start()
#
#
# def upload_progress(chunk):
#     up_progress.update(up_progress.currval + chunk)
#
#
# s3.upload_file(acc_file, bucketName, key, Callback=upload_progress(1))
# up_progress.finish()


# UPLOAD LOCATION FILE

body = {
    "fileName": "locexp.txt",
    "fileSize": 0,
    "fileType": "risk",
    "fileInputType": "MRI"
}

response_body = requests.post(url=f'{base_url}/storage/{bucketId}/path', headers=headers, json=body)
print(response_body.text)

accessKeyId = base64.b64decode(json.loads(response_body.text)["accessKeyId"]).decode("utf-8")
print(accessKeyId)
secretAccessKey = base64.b64decode(json.loads(response_body.text)["secretAccessKey"]).decode("utf-8")
print(secretAccessKey)
sessionToken = base64.b64decode(json.loads(response_body.text)["sessionToken"]).decode("utf-8")
print(sessionToken)
s3Path = base64.b64decode(json.loads(response_body.text)["s3Path"]).decode("utf-8")
print(s3Path)
s3Region = base64.b64decode(json.loads(response_body.text)["s3Region"]).decode("utf-8")
print(s3Region)
bucketName = s3Path.split("/")[0]
print(bucketName)
s3Path = s3Path[s3Path.index("/") + 1:]
print(s3Path)
fileName = body["fileName"]
print(fileName)
fileId.append(response_body.headers["Location"].split("/")[-1])
print(fileId)

s3 = boto3.client(
    's3',
    region_name=s3Region,
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretAccessKey,
    aws_session_token=sessionToken
)
key = s3Path + '/' + fileId[1] + '-' + fileName
print(key)

print("\n\nUPLOADING LOCATION FILE\n\n")

with open('.\\import_files\\locexp.txt', 'r') as f:
    content = f.read()
response_body = s3.put_object(Bucket=bucketName, Key=key, Body=content)
print(response_body)

# loc_file = '.\\import_files\\locexp.txt'
# with open(loc_file, "rb") as f:
#     file_upload = s3.upload_file(f, bucketName, key, Callback=ProgressPercentage(loc_file))
#

# UPLOAD MAPPING FILE

body = {
    "fileName": "map1.mff",
    "fileSize": 0,
    "fileType": "mapfile",
    "fileInputType": "MRI"
}

response_body = requests.post(url=f'{base_url}/storage/{bucketId}/path', headers=headers, json=body)
print(response_body.text)

accessKeyId = base64.b64decode(json.loads(response_body.text)["accessKeyId"]).decode("utf-8")
print(accessKeyId)
secretAccessKey = base64.b64decode(json.loads(response_body.text)["secretAccessKey"]).decode("utf-8")
print(secretAccessKey)
sessionToken = base64.b64decode(json.loads(response_body.text)["sessionToken"]).decode("utf-8")
print(sessionToken)
s3Path = base64.b64decode(json.loads(response_body.text)["s3Path"]).decode("utf-8")
print(s3Path)
s3Region = base64.b64decode(json.loads(response_body.text)["s3Region"]).decode("utf-8")
print(s3Region)
bucketName = s3Path.split("/")[0]
print(bucketName)
s3Path = s3Path[s3Path.index("/") + 1:]
print(s3Path)
fileName = body["fileName"]
print(fileName)
fileId.append(response_body.headers["Location"].split("/")[-1])
print(fileId)


s3 = boto3.client(
    's3',
    region_name=s3Region,
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretAccessKey,
    aws_session_token=sessionToken
)
key = s3Path + '/' + fileId[2] + '-' + fileName
print(key)

# AWS implementation of the ProcessPercentage
print("\n\nUPLOADING MAP FILE\n\n")

with open('.\\import_files\\map1.mff', 'r') as f:
    content = f.read()
response_body = s3.put_object(Bucket=bucketName, Key=key, Body=content)
print(response_body)

# map_file = '.\\import_files\\map1.mff'
# with open(map_file, "rb") as f:
#     print(f.read())
#     file_upload = s3.upload_file(f.read(), bucketName, key, Callback=ProgressPercentage(f))


# IMPORT

edm_name = 'RK_EDM'

print(fileId[0], type(fileId[0]))
print(fileId[1])
print(fileId[2])


body = {
    "accountsFileId": fileId[0],
    "locationsFileId": fileId[1],
    "reinsuranceFileId": None,
    "mappingFileId": fileId[2],
    "bucketId": bucketId,
    "delimiter": "TAB",
    "skipLines": 1,
    "dataSourceName": edm_name,
    "geoHaz": False,
    "appendLocations": False,
    "currency": "USD"
}

response_body = requests.post(url=f'{base_url}/imports/', headers=headers, json=body)
job = response_body.headers["Location"]
print(job)

response = requests.get(url=job, headers=headers)
while json.loads(response.text)["progress"] != 100:
    response = requests.get(url=job, headers=headers)
    print('Progress is {}%'.format(response_body.text["progress"]))

