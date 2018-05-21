## Some examples

**Simple text**

```
import matrix

matrix = matrix.Matrix()
matrix.text('F')
```

**Scrolling text with adjustable speed**

```
import matrix

matrix = matrix.Matrix()
matrix.scroll('Scrolling text example', s = 0.1)
```

**Display shape**

```
import matrix

matrix = matrix.Matrix()
shape = [[0,0,0,0,0,0,0,0], [0,1,1,0,0,1,1,0], [1,0,0,1,1,0,0,1], [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1], [0,1,0,0,0,0,1,0], [0,0,1,0,0,1,0,0], [0,0,0,1,1,0,0,0]]
matrix.shape(shape)
```

Or you can totally ignore `Matrix` class and write your own code by using the Max7219 class. You can find more under [examples] (https://github.com/7kmCo/micropython-max7219/tree/master/examples) directory.


## ESP32 Examples

```
import max7219
from machine import Pin, SPI
# Here the default pins for mosi and sck can be overritten.
spi = SPI(1, baudrate=14500000, sck=Pin(14), mosi=Pin(13))
display = max7219.Matrix8x8(spi, Pin(15), 4)
display.brightness(0)
display.fill(0)
display.text('1234',0,0,1)
display.show()
```

## ESP8266 Examples

Default baud rate of 80Mhz was introducing errors, dropped from 10Mhz and it works consistently.

```
import max7219
from machine import Pin, SPI
spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Matrix8x8(spi, Pin(15), 4)
display.brightness(0)
display.fill(0)
display.text('1234',0,0,1)
display.show()
```

## PyBoard Examples

**Single 8x8 LED Matrix**

```
import max7219
from machine import Pin, SPI
spi = SPI(1)
display = max7219.Matrix8x8(spi, Pin('X5'), 1)
display.text('1',0,0,1)
display.show()
```

**Chain of 4x 8x8 LED Matrices**
Where the 4 is drawn on the DIN matrix.

```
import max7219
from machine import Pin, SPI
spi = SPI(1)
display = max7219.Matrix8x8(spi, Pin('X5'), 4)
display.text('1234',0,0,1)
display.show()
```

**Chain of 8x 8x8 LED Matrices**
Where the 8 is drawn on the DIN matrix

```
import max7219
from machine import Pin, SPI
spi = SPI(1)
display = max7219.Matrix8x8(spi, Pin('X5'), 8)
display.text('12345678',0,0,1)
display.show()
```

**Framebuf shapes and text**

```
display.fill(0)
display.show()

display.pixel(0,0,1)
display.pixel(1,1,1)
display.hline(0,4,8,1)
display.vline(4,0,8,1)
display.line(8, 0, 16, 8, 1)
display.rect(17,1,6,6,1)
display.fill_rect(25,1,6,6,1)
display.show()

display.fill(0)
display.text('dead',0,0,1)
display.text('beef',32,0,1)
display.show()

display.fill(0)
display.text('12345678',0,0,1)
display.show()
display.scroll(-8,0) # 23456788
display.scroll(-8,0) # 34567888
display.show()
```