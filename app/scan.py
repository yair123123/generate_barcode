from pyzbar.pyzbar import decode

import cv2

from app.create_barcode import BarcodeReader, generate_barcode, generate


def scan():
    cam = cv2.VideoCapture(0)

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
    while True:
        ret, frame = cam.read()
        for barcode in decode(frame):
            # BarcodeReader(frame)
            barcode_data = barcode.data.decode("utf-8")
            generate(barcode_data)
            print(f"Scan BarCode: {barcode_data}")
            return barcode_data
        out.write(frame)

        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    out.release()
    cv2.destroyAllWindows()


scan()
