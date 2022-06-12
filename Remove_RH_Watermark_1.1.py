#!/usr/bin/python
from pdfrw import PdfReader, PdfWriter
import sys

with open(sys.argv[1], "rb") as pdf_file:
    reader = PdfReader(pdf_file)

    for page in reader.pages:
        x_object = page.Resources.XObject
        
        for obj in x_object:
            if x_object[obj]["/Subtype"] == "/Image" and ("/SMask" in x_object[obj]) and (x_object[obj]["/Height"] == "990" or x_object[obj]["/Height"] == "1"):
                x_object[obj].update({'/Width': '0'})
            elif x_object[obj]["/Subtype"] == "/Image" and x_object[obj]["/Height"] == "990" and x_object[obj]["/Width"] == "765":   
                x_object[obj].update({'/Width': '0'})
    
    PdfWriter().write(sys.argv[1] + ".pdf", reader)