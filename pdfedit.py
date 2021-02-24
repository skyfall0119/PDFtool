#Requires the “PyPDF2” and “OS” modules to be imported
import os, PyPDF2





# receive filelist, userfilename
# output combining all pdf file contained in filelist in order.

def pdf_combine(filelist, userfilename):
  #Get all the PDF filenames
  pdf2merge = []
  for filename in filelist:
    if filename.endswith(".pdf"):
      pdf2merge.append(filename)

  pdfWriter = PyPDF2.PdfFileWriter()

  #loop through all PDFs
  for filename in pdf2merge:
    #rb for read binary
    pdfFileObj = open(filename,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):
      pageObj = pdfReader.getPage(pageNum)
      pdfWriter.addPage(pageObj)
  #save PDF to file, wb for write binary
  pdfOutput = open(userfilename+".pdf", "wb")
  #Outputting the PDF
  pdfWriter.write(pdfOutput)
  #Closing the PDF writer
  pdfOutput.close()



# image to pdf
# https://datatofish.com/images-to-pdf-python/

# pdf combine
# https://geektechstuff.com/2018/02/17/python-3-merge-multiple-pdfs-into-one-pdf/



# pageNum = second file start page
def pdf_split(file, splitNum, userfilename1, userfilename2):
    pdfWriter1 = PyPDF2.PdfFileWriter()
    pdfWriter2 = PyPDF2.PdfFileWriter()

    #rb for read binary
    pdfFileObj = open(file,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):

        # if under selected page
        if pageNum < splitNum:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter1.addPage(pageObj)
        else: 
            # if selected or later page
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter2.addPage(pageObj)


    #save PDF to file, wb for write binary
    pdfOutput1 = open(userfilename1+".pdf", "wb")
    pdfOutput2 = open(userfilename2+".pdf", "wb")
    #Outputting the PDF
    pdfWriter1.write(pdfOutput1)
    pdfWriter2.write(pdfOutput2)

    #Closing the PDF writer
    pdfOutput1.close()
    pdfOutput2.close()


#takeoutNum is list of number

def pdf_takeout(file, takeoutNum, userfilename):
    pdfWriter = PyPDF2.PdfFileWriter()


    #rb for read binary
    pdfFileObj = open(file,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):

        # if takeout page
        if pageNum not in takeoutNum:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)


    #save PDF to file, wb for write binary
    pdfOutput = open(userfilename+".pdf", "wb")
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()

