import qrcode
qr=qrcode.QRCode(
    version=1,
    box_size=12,
    border=6
    )

data="Hello everyone! I am a qrcode" #if you want to add any link you can use 'link'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("1.png")
