import unittest
import base64
from io import BytesIO
import io
from PIL import Image
import img

class TestImgEntity(unittest.TestCase):
    def setUp(self):
        self.dummyImg = Image.new("RGB",(150,50),(255,255,255))
        imageFileObj = BytesIO()
        self.dummyImg.save(imageFileObj,format="JPEG")
        self.data = imageFileObj.getvalue()
        imageFileObj.close()

    def test_convert_base64(self):
        expected = base64.b64encode(self.data)
        test_img = img.CustomImage.fromBytes(self.data)

        b64_result = test_img.toBase64()

        self.assertEqual(expected,b64_result)
    def test_resize_W_keeping_aspect_ratio(self):
        new_width = 120
        expected = (120,40)
        test_img = img.CustomImage.fromBytes(self.data)

        test_img.resizeW(120)

        self.assertEqual(expected,test_img.get_dimensions())
        


if __name__ == "__main__":
    unittest.main()
