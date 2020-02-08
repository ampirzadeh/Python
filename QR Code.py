import pyqrcode

url = pyqrcode.create("Bardia")
url.svg('qr.svg',scale=8)
print(url.terminal(quiet_zone=1))