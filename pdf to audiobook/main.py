import pyttsx3
import PyPDF2
import pdfplumber
from tkinter.filedialog import *

file= askopenfilename()
# pdfreader = PyPDF2.PdfFileReader(book)

# pages=pdfReader.numPages
# for i in range(0,1):        
#         page=pdfreader.getPage(i)
#         text=page.extract_text()
#         print(text)
#         player = pyttsx3.init()
#         player.say(text)
#         player.runAndWait()



# file='test_file.pdf'


pdfFileObj = open(file, 'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# print(pdfreader.documentInfo)
pages=pdfReader.numPages
print(pdfReader.numPages)
with pdfplumber.open(file) as pdf:
    for i in range(0,pages):        
        page=pdf.pages[i]
        text=page.extract_text()
        print(text)
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()