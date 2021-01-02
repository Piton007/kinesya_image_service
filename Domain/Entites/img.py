from PIL import Image
from io import BytesIO
from base64 import b64encode


IMAGE_FORMAT = 'RGBA' 
class CustomImage:
    
    @staticmethod
    def fromBytes(data):
        return CustomImage(Image.open(BytesIO(data)))

    def __init__(self,img):
        self.img = img
    
    @property
    def size(self):
        return self.img.size
    
    def resizeW(self,width):
        w,h = self.img.size
        wpercent = (width / float(w))
        hsize = int(float(h) * float(wpercent))
        self.img = self.img.resize((width,hsize),Image.LANCZOS) 
    def clone(self):
        return CustomImage.fromBytes(self.toBytes)
    
    def toBytes(self):
        return self.img.tobytes()


    def toBase64(self):
        buff = BytesIO()
        self.img.save(buff,format="JPEG")
        return b64encode(buff.getvalue()) 