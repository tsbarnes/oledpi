from driver import SPI, SSD1305
from PIL import Image, ImageDraw, ImageFont


class Display:
    height: int = 32
    width: int = 128
    spi: SPI.SpiDev = None
    oled: SSD1305.SSD1305_128_32 = None

    def __init__(self):
        self.spi = SPI.SpiDev(0, 0, max_speed_hz=1000000)
        self.oled = SSD1305.SSD1305_128_32(rst=None, dc=24, spi=self.spi)
        self.oled.begin()
        self.oled.clear()
        self.oled.display()

    def draw_image(self, image: Image):
        if image.size != (self.width, self.height):
            raise ValueError("Image must be {}x{}".format(self.width, self.height))
        self.oled.image(image)
        self.oled.display()
