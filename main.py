from pdf2docx import Converter
input_path="sample.pdf"
output_path="sample.docx"

cv=Converter(pdf_file=input_path)
cv.convert(docx_filename=output_path)
cv.close()

