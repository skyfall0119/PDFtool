#Requires the “PyPDF2” and “OS” modules to be imported
import os, PyPDF2
import img2pdf





# receive filelist, userfilename
# output combining all pdf file contained in filelist in order.

def pdf_combine(filelist, userfilename):
  
  #Get all the PDF filenames

  ext = [".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG"]
  pdfmerger = PyPDF2.PdfFileMerger()

  #loop through all PDFs
  for filename in filelist:
    #rb for read binary
    if filename.endswith(".pdf"):
      pdfFileObj = open(filename,"rb")
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

      pdfmerger.append(pdfReader)


    elif filename.endswith(tuple(ext)):
      pdfbytes = img2pdf.convert(filename)
      pdfn = filename.split('.')[0]+".pdf"
      f = open(pdfn, 'wb+')
      f.write(pdfbytes)
      pdfmerger.append(fileobj=f)

    else:
      raise Exception("Invalid File Type")





  #save PDF to file, wb for write binary
  pdfOutput = open(userfilename+".pdf", "wb")
  #Outputting the PDF
  pdfmerger.write(pdfOutput)
  #Closing
  f.close()
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

    # if not isinstance(splitNum, int):
    #   raise Exception("put valid number")

    if pdfReader.numPages < max(splitNum)  or min(splitNum) < 1  or len(splitNum) > 1:
      raise Exception("Error on Page Number")
  

    num = splitNum[0]

    #Opening each page of the PDF
    for pageNum in range(pdfReader.numPages):

        # if under selected page
        if pageNum < num:
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


#extract pages Num is list of number

def pdf_extract(file, extractNum, userfilename):
    pdfWriter = PyPDF2.PdfFileWriter()


    #rb for read binary
    pdfFileObj = open(file,"rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #Opening each page of the PDF
    
    if pdfReader.numPages < max(extractNum) or min(extractNum) < 0:
      raise Exception("Error on Page Number")

    for pageNum in range(pdfReader.numPages):

        # if extract page
        if pageNum in extractNum:
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)


    #save PDF to file, wb for write binary
    pdfOutput = open(userfilename+".pdf", "wb")
    #Outputting the PDF
    pdfWriter.write(pdfOutput)
    #Closing the PDF writer
    pdfOutput.close()


