# Assignment 10

# Contact Tracing App
#	- Create a python program that will read QRCode using your webcam
#	- You may use any online QRCode generator to create QRCode
#	- All personal data are in QRCode 
#	- You may decide which personal data to include
#	- All data read from QRCode should be stored in a text file including the date and time it was read


# QR Code Scanner
import cv2
import webbrowser
import datetime
from pyzbar.pyzbar import decode


vidcap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = vidcap.read()
    data, one, _ = detector.detectAndDecode(img)
    if data:
        read = data
        # Record Date and Time of QR Code Detection
        with open("qrscanrecords.txt", mode='a') as file:
            file.write(f'Scanned QR Code redirecting to {read} recorded at %s.\n' % 
               (datetime.datetime.now()))
        break
    for barcode in decode(img):
        text = barcode.data.decode('utf-8')
        print(text)
        with open("qrscanrecords.txt", mode='a') as file:
            file.write(f'Scanned QR Code containing {text} recorded at %s.\n' % 
            (datetime.datetime.now())) 
            vidcap.release(text)
            cv2.destroyAllWindows
        break
    cv2.imshow('QRCode Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
redirect = webbrowser.open((str(read)))
vidcap.release(read)
cv2.destroyAllWindows



