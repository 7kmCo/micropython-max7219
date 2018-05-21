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

  # Scrolling text. I was not able to make official scroll method work,
  # also on the website they warn "This may leave a footprint of the previous colors in the FrameBuffer."
  # So I wrote this simple method which speed is adjustable.
  # For now, I'm waiting for my other led matrixes to arrive, then I can test further and add more options like scroll direction and etc.
  def scroll(self, txt, s = 0.5, c = 1):
    text_len = len(txt) * 8 + 8
    while True:
      for i in range(text_len):
        self.text(txt, 8 - i)
        sleep(s)
      sleep(s)

  # Draw a shape. all this needs is to set shape pattern.
  # For example [[0,0,0,0,0,0,0,0], [0,1,1,0,0,1,1,0], [1,0,0,1,1,0,0,1], [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1], [0,1,0,0,0,0,1,0], [0,0,1,0,0,1,0,0], [0,0,0,1,1,0,0,0]] will display a heart
  def shape(self, patern = [], delay = 0):
    self.display.fill(0)
    for li, l in enumerate(patern):
      for di, d in enumerate(l):
        if d == 1:
          sleep(delay)
          self.display.pixel(int(di), int(li), 1)
          self.display.show()