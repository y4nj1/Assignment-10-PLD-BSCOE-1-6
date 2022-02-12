# Create QR Code
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
link = "https://github.com/y4nj1"
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("sampleqr.png")

# QR Code Scanner
import cv2
import webbrowser
import datetime

vidcap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = vidcap.read()
    data, one, _ = detector.detectAndDecode(img)
    if data:
        read = data
        # Record Date and Time of QR Code Detection
        with open("qrscanrecords.txt", mode='a') as file:
            file.write(f'Scanned QR Code redirecting to {link} recorded at %s.\n' % 
               (datetime.datetime.now()))
        break
    cv2.imshow('QRCode Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
redirect = webbrowser.open((str(read)))
vidcap.release(read)
cv2.destroyAllWindows




