import qrcode

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)

data = input('Data : ')
qr.add_data(data)
qr.make(fit = True)
qrCode = qr.make_image(fill = 'black', back_color="white")
qrCode.save('QR-Code.png')
print('\nSaved as "QrCode.png"')