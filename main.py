#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import time
import os
import sys
import distro
import psutil

from display import Display

try:
    from local_settings import FONT
except ImportError:
    FONT = None


class App:
    display: Display = None
    image: Image = None
    draw: ImageDraw = None
    font: ImageFont = None

    def __init__(self):
        self.display = Display()
        self.image = Image.new('1', (self.display.width, self.display.height), color=0)
        self.draw = ImageDraw.Draw(self.image)
        if FONT:
            self.font = ImageFont.truetype(FONT, 8)
        else:
            self.font = ImageFont.load_default()
        self.display.draw_image(self.image)

    def run(self):
        while True:
            time.sleep(1)
            self.draw.rectangle((0, 0, self.display.width, self.display.height), outline=0, fill=0)

            self.draw.text((0, 0), "CPU: " + str(psutil.cpu_percent()) + "%", font=self.font, fill=255)
            self.draw.text((0, 8), "MEM: " + str(psutil.virtual_memory().percent) + "%", font=self.font, fill=255)
            self.draw.text((0, 16), "DISK: " + str(psutil.disk_usage('/').percent) + "%", font=self.font, fill=255)
            self.draw.text((0, 24), "OS: " + distro.name(pretty=True), font=self.font, fill=255)

            self.display.draw_image(self.image)


if __name__ == '__main__':
    app = App()
    app.run()
