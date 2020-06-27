import subprocess as sub 
from subprocess import Popen

LIBRE_OFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"
 

def convert_to_pdf(input_docx, out_folder):
    p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir',
               out_folder, input_docx])
    print([LIBRE_OFFICE, '--convert-to', 'pdf', input_docx])
    p.communicate()

sample_doc = r'C:\Users\ThanhTiem\Desktop\testpy\CAI_TIEN_OCR.docx'
out_pdf = r'C:\Users\ThanhTiem\Desktop\test'
convert_to_pdf(sample_doc, out_pdf)