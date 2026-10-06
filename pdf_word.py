import os
from pdf2docx import Converter

input_folder = 'input_pdfs'
output_folder = 'output_docs'
files = os.listdir(r"C:\\Users\\mmotlaq\\Desktop\\pdf2word\\input_pdfs")

for file in files:
    if file.lower().endswith('.pdf'):
        pdf_path = os.path.join(input_folder, file)
        docx_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.docx')

        
        my_conv = Converter(pdf_path)
        my_conv.convert(docx_path)
       
print('Convert Done')
