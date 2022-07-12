# REFERENCE
# https://stackoverflow.com/questions/2925484/place-image-over-pdf

from PyPDF2 import PdfFileWriter, PdfFileReader, Transformation
from reportlab.pdfgen import canvas

imCoors_mm = [[113, 165], [113, 165], [260, 170], [107, 20], [107, 20], [107, 20], [107, 20], [107, 20], [107, 20]]
imDims_mm = [[0, 0], [22, 27], [24, 29], [23, 27], [22, 27], [22, 27], [22, 27], [22, 27], [22, 27]]

def mm2pts(mm):
    return mm*2.83464567 


def createWatermark(imgPath):
    # Create the watermark from an image
    c = canvas.Canvas('temp_watermark.pdf')
    c.setPageSize((mm2pts(297), mm2pts(210)))

    # Draw the image at x, y. I positioned the x,y to be where i like here
    for imCoor, imDim in zip(imCoors_mm, imDims_mm):
        c.drawImage(imgPath, mm2pts(imCoor[0]), mm2pts(imCoor[1]), mm2pts(imDim[0]), mm2pts(imDim[1]))
        c.showPage()

    c.save()

def addWatermark():
    # Get the watermark file you just created
    watermark = PdfFileReader(open("temp_watermark.pdf", "rb"))

    # Get our files ready
    output_file = PdfFileWriter()
    input_file = PdfFileReader(open("raw.pdf", "rb"))

    # Number of pages in input document
    page_count = input_file.getNumPages()

    # Go through all the input file pages to add a watermark to them
    for page_number in range(page_count):
        print ("Watermarking page {} of {}".format(page_number, page_count))
        # merge the watermark with the page
        input_page = input_file.getPage(page_number)
        input_page.mergePage(watermark.getPage(page_number))
        # add page from input file to output document
        output_file.addPage(input_page)

    # finally, write "output" to document-output.pdf
    with open("document-output.pdf", "wb") as outputStream:
        output_file.write(outputStream)

if __name__ == "__main__":
    createWatermark("photo.jpg")
    addWatermark()