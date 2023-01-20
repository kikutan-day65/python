"""
command line:
>>> py combine.py pdf1 pdf2 pdf3 ... pdfn
"""

import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")

pdf_combiner(inputs)