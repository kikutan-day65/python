import PyPDF2

"""
# check if the file exists in that path
import os
path = ".\\pdfs\\dummy.pdf"
if os.path.exists:
    print("OK")
else:
    print("no")
"""


with open(".\\pdfs\\dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(reader.numPages)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
