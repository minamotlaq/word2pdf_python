import requests
import json

url = "https://www.eboo.ir/api/ocr/getway"


payload = {
"token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"command": "addfile",
"filelink": "http://www.yourwebsite.com/File.pdf"
}
response = requests.post(url, data=payload)




filename = "C:\\Users\\Username\\Desktop\\File.pdf"
upload = {'filehandle':(filename, open(filename, 'rb'), 'multipart/form-data')}
payload = {
"token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"command": "addfile",
}



response = requests.post(url, data=payload,files=upload)


data = response.text


json_data = json.loads(data)


print(json.dumps(json_data, indent=4))