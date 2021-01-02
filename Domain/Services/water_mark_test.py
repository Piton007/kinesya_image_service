import sys
sys.path.append("D:\Projects\kinesya_serviceimage\Domain\Entites")
import unittest
import base64
from io import BytesIO
from PIL import Image
from img import CustomImage
from water_mark import WaterMarkDrawer




class TestWaterMarkService(unittest.TestCase):
    def setUp(self):
        self.dummyImg = Image.new("RGB",(150,100),(255,255,255))
        imageFileObj = BytesIO()
        self.dummyImg.save(imageFileObj,format="JPEG")
        self.data = imageFileObj.getvalue()
        imageFileObj.close()
        self.__setUp_watermark()
    def __setUp_watermark(self):
        self.watermark = Image.new("RGB",(400,200),(255,255,255))
        imageFileObj = BytesIO()
        self.watermark.save(imageFileObj,format="JPEG")
        self.watermark_data = imageFileObj.getvalue()
        imageFileObj.close()

    def test_calculate_water_mark_position(self):
        expected = (0 , 12)
        watermark = CustomImage.fromBytes(self.watermark_data)
        watermark.resizeW(self.dummyImg.size[0])
        drawer = WaterMarkDrawer(self.watermark_data)

        result = drawer.calculate_watermark_pos(self.dummyImg,watermark)
        self.assertEqual(expected,result)



if __name__ == "__main__":
    unittest.main()
