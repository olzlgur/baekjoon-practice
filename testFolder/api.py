import requests
import json

token = "a4cfc65f6dc4c1913bfa9fe9061563f2"
auth_key = "40fa8edc-0812-423d-999d-2f44adca0b00"
# url = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/start"
url = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/new_requests"

headers = {'Content-Type': 'application/json', 'Authorization': auth_key}
# headers = {'Content-Type': 'application/json', 'X-AUTH-TOKEN': token}
body = {
    "problem": 2
}

# response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
response = requests.get(url, headers=headers)

jsonObject = json.loads(response.content)
print(jsonObject)
# print(jsonObject.get('reservations_info')[0].get('id'))

