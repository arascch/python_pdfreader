import PyPDF2

pdffileobject = open('pdffile.pdf' , 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobject)
print(pdfreader.numPages)
pageObj = pdfreader.getPage(0)
print(pageObj.extractText())
pdffileobject.close()