from PIL import Image
import img as Img
from io import BytesIO

class WaterMarkDrawer(object):

    def __init__(self,watermark):
        self.watermark = watermark
    
    def add_watermark(self,base_image):
        w_base,h_base = base_image.size
        self.watermark.resizeW(w_base)
        wm_pos= self.calculate_watermark_pos(base_image)
        new_image = Image.new('RGBA', base_image.size, (0,0,0,0))
        new_image.paste(base_image.img, (0,0))
        new_image.paste(self.watermark.img,wm_pos,mask=self.watermark.img)
        buff = BytesIO()
        new_image.save(buff,format="PNG")
        return Img.CustomImage.fromBytes(buff.getvalue())

    def calculate_watermark_pos(self,base_image):
        w_base,h_base = base_image.size
        return (0, (h_base - self.watermark.size[1]) // 2) 

        

