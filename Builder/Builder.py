import qrcode

class QrCode:
    def __init__(self):
        self.qr = qrcode.QRCode(
            box_size=10,
            border=4
        )
        self.image = ''
        
    def generator(self, text):
        self.image = self.qr.add_data(text)
        self.image = self.qr.make_image()

    def save(self,path,ext=".png",name="noname"):
        self.image.save(path+name+ext)