# Remove_Redhat_watermark
As you know, student workbook pdf file downloaded from Redhat learning website will always come with a watermark which include your email information, I really don't like the watermark, this is a python script to remove watermark of redhat student workbook pdf file, you can use it at your own risk.

This script requires pdfrw module, and has been tested in Python 3.8.

`% python3 Remove_RH_Watermark_1.1.py DO180-OCP4.5-en-3-20201217.pdf`

If it is successful, you will see the new file without watermark with a filename with additional ".pdf".

There is a known issue that the new file will be prompted with a message "An error exists on this page. Acrobat may not display the page correctly. Please contact the person who created the PDF document to correct the problem.", I guess it is related to pdfrw module, I have no clue to fix it.
