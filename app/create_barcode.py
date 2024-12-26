# Importing library
import cv2
from pyzbar.pyzbar import decode
from barcode import EAN13

# Make one method to decode the barcode
def BarcodeReader(img):
    # read the image in numpy array using cv2

    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

            # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode(data, filename="barcode"):
    barcode = Code128(data, writer=ImageWriter())
    barcode.save(filename)
    print(f"Barcode saved as {filename}.png")

def generate(data):
    code = EAN13(data)
    code.save("code")