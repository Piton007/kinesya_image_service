from PIL import Image
import img as Img

class WaterMarkDrawer(object):

    def __init__(self,watermark_data):
        self.watermark_data = watermark_data
    
    def add_watermark(self,base_image):
        w_base,h_base = base_image.size
        watermark = Img.CustomImage.fromBytes(self.watermark_data)
        watermark.resizeW(base_image)
        wm_pos= self.calculate_watermark_pos(base_image,watermark)
        new_image = Image.new('RGBA', base_image.size, (0,0,0,0))
        new_image.paste(base_image, (0,0))
        new_image.paste(watermark,wm_pos,mask=watermark)
        return Img.CustomImage.fromBytes(new_image.tobytes())

    def calculate_watermark_pos(self,base_image,watermark):
        w_base,h_base = base_image.size
        return (0, (h_base - watermark.size[1]) // 2) 

        

