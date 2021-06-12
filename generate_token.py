import requests
import json

auth_url = 'https://api-euw1.rms.com/sml/auth/v1/Login/implicit'
tenantName = 'customersuccess'
user = 'rohit.kumar@rms.com'
password = 'Q6CGHw-jQ66a&=mF'

body = {
    "tenantName": tenantName,
    "username": user,
    "password": password
}


with open("token.txt") as file:
    token = file.readline().strip()

headers = {
    "Authorization": f"Bearer {token}"
}


def get_token():
    response_body = requests.get(url='https://api-euw1.rms.com/riskmodeler/v1/domains', headers=headers)
    if response_body.text == '{"message":"Unauthorized"}':
        response_body = requests.post(url=auth_url, json=body)

        with open("token.txt", "w") as file:
            print(json.loads(response_body.text)["accessToken"], file=file)


with open("token.txt") as file:
    token = file.readline().strip()

headers = {
    "Authorization": f"Bearer {token}"
}
