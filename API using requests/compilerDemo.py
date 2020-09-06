import requests
import json
headers={'Content-type':'application/json', 'Accept':'application/json'}

payload = {

    'script':"print(5+3)",
    'language': "python3",
    'versionIndex': "3",
    'clientId': "f239f30780ae492d1c4a34543395e688",
    'clientSecret':"403da617b9be15fb26e2fd75bb493697b3cbd0d2d5dbc760ecbbabbca03a4829"
}

r = requests.post('https://api.jdoodle.com/v1/execute',json=payload,headers=headers)
r_dict = r.text
data = json.loads(r_dict)
print(data['output'])