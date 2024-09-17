from PyPDF2 import PdfReader, PdfWriter
# import io
# import os
from PDF_compressor.pdf_compressor import compress

def compress_pdf(input_file, output_file):
    # reader = PdfReader(input_file)
    # writer = PdfWriter()

    # for page in reader.pages:
    #     page.compress_content_streams()  # This is CPU intensive!
    #     writer.add_page(page)

    # output_buffer = io.BytesIO()
    # with open(output_file, "wb") as f:
    #     writer.write(f)
    # print(os.path.isfile(input_file))
    compress(input_file,output_file,power=4)

