import PyPDF2
import os

print("\n\nWelcome to the pdfMerger\n\n")
print("-----------------------------------------------------------------\n\n")
print("How to use\n\n\n")
print("Step 1: Create a folder and add all the pdf files that you want to merge in that folder\n\n")
print("Step 2: Copy this pdfMerger.exe file (that you just clicked) into that folder\n\n")
print("Step 3: pdfMerger merges files in alphabetic order of their names\n\n")
print("For example: Four pdf files named: Airline, 7rules, Train and bus will be merged in the following order\n\n")
print("7rules, Airline, bus, Train\n\n")
print("Step 4: If needed rename file names to match the order in which it needs to be merged\n\n")
print("------------------------------------------------------------------\n\n")

print("If you need to perform any of the prerequisite steps mentioned above\nyou can close this window and come back after performing the steps\n\n")

print("--------------------Merging process starts here-----------------\n\n\n")

print("Enter a name for the final merged PDF\n")
print("Note: Make sure no file with the same name exists in the current folder\n")
finalFileName = input()
outputFile = finalFileName + '.pdf'

while os.path.isfile('./' + outputFile):
    print("A pdf file with the exact same name already exists in this folder\n")
    print("Please try some other name")
    finalFileName = input()
    outputFile = finalFileName + '.pdf'
    
allPdfFilesInFolder = []

for fileName in os.listdir('.'):
    if fileName.endswith('.pdf'):
        allPdfFilesInFolder.append(fileName)

allPdfFilesInFolder.sort(key = str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for fileName in allPdfFilesInFolder:
    pdfFileObject = open(fileName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    for page in range(0, pdfReader.numPages):
        pageObject = pdfReader.getPage(page)
        pdfWriter.addPage(pageObject)

pdfOutput = open(outputFile, 'wb')
pdfWriter.write(pdfOutput)

print("Your pdfs have been merged and a new merged PDF by the name " + finalFileName + " has been created in the same folder\n");
print("Press Enter key to exit this program before opening the newly created " + finalFileName + " file\n")
ex = input()

pdfOutput.close()




