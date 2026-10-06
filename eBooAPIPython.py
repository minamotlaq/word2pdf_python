import requests
import json

url = "https://www.eboo.ir/api/ocr/getway"


########### ارسال از طریق لینک
payload = {
"token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"command": "addfile",
"filelink": "http://www.yourwebsite.com/File.pdf"
}
response = requests.post(url, data=payload)



########### ارسال از طریق آپلود فایل
filename = "C:\\Users\\Username\\Desktop\\File.pdf"
upload = {'filehandle':(filename, open(filename, 'rb'), 'multipart/form-data')}
payload = {
"token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"command": "addfile",
}


# ارسال درخواست
response = requests.post(url, data=payload,files=upload)

# دریافت خروجی
data = response.text

# دریافت Json
json_data = json.loads(data)

# نمایش داده
print(json.dumps(json_data, indent=4))