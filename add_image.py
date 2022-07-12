# REFERENCE
# https://stackoverflow.com/questions/2925484/place-image-over-pdf

from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from msvcrt import getch

imCoors_mm = [[0, 0], [105, 162], [260, 169], [113, 168], [260, 169], [113, 168], [0, 0], [0, 0], [113, 168]]
imDims_mm = [[0, 0], [24, 29], [24, 29], [24, 29], [24, 29], [24, 29], [0, 0], [0, 0], [24, 29]]

def mm2pts(mm):
    return mm*2.83464567 


def createWatermark(imgPath):
    print("Preparing photo...")
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
        print (f"Adding photo to page {page_number + 1} of {page_count}")
        # merge the watermark with the page
        input_page = input_file.getPage(page_number)
        input_page.mergePage(watermark.getPage(page_number))
        # add page from input file to output document
        output_file.addPage(input_page)

    # finally, write "output" to document-output.pdf
    with open("document-output.pdf", "wb") as outputStream:
        output_file.write(outputStream)

if __name__ == "__main__":
    try:
        createWatermark("photo.jpg")
        addWatermark()
        print("--> Photos successfully added!")
        print("--> See 'document-output.pdf'")
    except Exception as ex:
        print("An error occured:")
        print(ex)
    finally:
        print("Press any key to exit...")
        getch()