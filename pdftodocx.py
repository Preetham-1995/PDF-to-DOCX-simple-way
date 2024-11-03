from pdf2docx import Converter

pdf_file = input("Enter the name of the PDF file (including .pdf extension): ") # Single click on the pdf file and enter (ctrl+c)

import os
if not os.path.isfile(pdf_file):
    print("The specified file does not exist. Please check the file name and try again.")
else:
    docx_file = pdf_file.replace('.pdf', '.docx')
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
    print(f"Conversion complete! The DOCX file is saved as: {docx_file}")
