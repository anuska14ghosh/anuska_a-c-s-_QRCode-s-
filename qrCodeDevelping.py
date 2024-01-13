import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size= 10, border= 5)
qr.add_data("https://vsco.co/anuskaghosh14/gallery")
qr.make(fit=True)
img= qr.make_image(fill_color= "brown", back_color= "beige")
img.save("Anuska_Online_photo_Gallery.png")