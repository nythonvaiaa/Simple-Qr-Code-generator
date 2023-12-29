import qrcode as qr
image=qr.make("https://www.youtube.com/@nythonvaiaa")
image.save("image.png")