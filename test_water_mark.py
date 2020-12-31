import unittest
import base64
import io
from PIL import Image



class TestWaterMarkService(unittest.TestCase):
    def test_calculate_water_mark_position(self):
        p_width,p_height = (400,600)
        wm_width,wm_height = (400,30)
        expected = [0,285]

        posX,posY = 0, (p_height - wm_height) // 2 
        self.assertEqual([posX,posY],expected)


if __name__ == "__main__":
    unittest.main()
