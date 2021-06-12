import json

import requests
with open("token.txt") as file:
    token = file.readline().strip()

headers = {
    "Authorization": f"Bearer {token}"
}

job = 'https://api-euw1.rms.com/riskmodeler/v1/workflows/2886856'

response_body = requests.get(url=job, headers=headers)
while json.loads(response_body.text)["progress"] != 100:
    response_body = requests.get(url=job, headers=headers)
    print('Progress is {}%'.format(response_body.text["progress"]))

