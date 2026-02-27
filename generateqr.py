import qrcode
url=input("Enter the URL or text to generate QR code: ")
img=qrcode.make(url)
img.save("qrcode.png")
print("QR code saved as qrcode.png")