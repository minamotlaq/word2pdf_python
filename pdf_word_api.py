import os
import requests
import sys


API_URL = "https://www.eboo.ir/api/ocr/getway"
TOKEN = "HHqna7Stw6wEUxw2AsjiDoAYmu9blmJs"


InputDIR = r"C:\\Users\\mmotlaq\\Desktop\\pdf2word\\pdf2word\\input_pdfs"
OutDIR = r"C:\\Users\\mmotlaq\\Desktop\\pdf2word\\pdf2word\\output_docs"

def upload_pdf(file_path):
    payload = {
        "token": TOKEN,
        'command': 'addfile',
    }
    with open(file_path, 'rb') as f:
        files = {'filehandle': (os.path.basename(file_path), f, "application/pdf")}
        res = requests.post(API_URL, data=payload, files=files)
        res_json = res.json()
    
    if res_json.get('Status') == 'Done':
        return res_json.get('FileToken')
    else:
        print(' NOT upload ')
        return None

def convert_pdf(filetoken):
    payload = {
        'token': TOKEN,
        'command': 'convert',
        'filetoken': filetoken,
        'method': 3,
        'output': 'keeplayout',
    }
    res = requests.post(API_URL, json=payload, timeout=600)
    return res.json()

def download_file(url, save_path):
    with open(save_path, 'wb') as f:
        res = requests.get(url)
        f.write(res.content)
        print(f' file saved  : {save_path}')

# daryaft argoman az khat farman
if len(sys.argv) > 3:
    InputDIR = sys.argv[1]
    OutDIR = sys.argv[2]
    TOKEN = sys.argv[3]

print(f'input: {InputDIR}')
print(f'output: {OutDIR}')

# ejad folder kho darsoorat adam vojood
if not os.path.exists(OutDIR):
    os.makedirs(OutDIR)
# list file
files = os.listdir(InputDIR)

for file in files:
    if file.lower().endswith('.pdf'):
        pdf_path = os.path.join(InputDIR, file)
        docx_path = os.path.join(OutDIR, os.path.splitext(file)[0] + '.docx')
        
        print(f' in process : {file}')
        
        # upload
        filetoken = upload_pdf(pdf_path)
        
        if filetoken:
            print(f' token receive  : {filetoken}')
            
            # tabdil
            print('converting...')
            out = convert_pdf(filetoken)
            
            # download
            output_url = out.get('FileToDownload')
            if output_url:
                download_file(output_url, docx_path)
            else:
                print('not find link')
        else:
            print('erro')
        
        print('-' * 20)

print('convert Done')

    
