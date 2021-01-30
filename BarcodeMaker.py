import barcode
from barcode.writer import ImageWriter

value = input('Data : ')
hr = barcode.get_barcode_class('code39')
Hr = hr(value, writer = ImageWriter())
qr = Hr.save('barcode')
print('\nDone')