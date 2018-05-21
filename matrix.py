# This is a helper class to make working with LED matrixes easier

import max7219
from machine import Pin, SPI
from time import sleep

class Matrix:
  def __init__(self, cspin = 15, sckpin = 14, mosipin = 13, num = 1):
    spi = SPI(1, baudrate=14500000, sck = Pin(int(sckpin)), mosi = Pin(int(mosipin)))
    self.display = max7219.Max7219(spi, Pin(int(cspin)), num)
    self.display.brightness(0)

  # Display normal text
  def text(self, txt, x = 0, y = 0, c = 1):
    self.display.fill(0)
    self.display.text(txt, x, y, c)
    self.display.show()
