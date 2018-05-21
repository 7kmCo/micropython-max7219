# MicroPython MAX7219 8x8 LED Matrix

A MicroPython library for the MAX7219 8x8 LED matrix driver, SPI interface, supports cascading and uses [framebuf](http://docs.micropython.org/en/latest/pyboard/library/framebuf.html)


## How to use

```
import matrix

matrix = matrix.Matrix()
matrix.text('F')
```

At the moment, only three methods (text, scroll and shape) added to the `Matrix` class whitch samples can be found in `/examples` directory, more will be added later. Fill free to make suggestions, pull requests are wellcome.

Or you can totally ignore `Matrix` class and write your own code by using the Max7219 class. You can find more under [examples] (https://github.com/7kmCo/micropython-max7219/tree/master/examples) directory.

## Connections


### Connections for ESP8266 or ESP32, The pins can be changed while initiating the class.

Wemos D1 Mini    | max7219 8x8 LED Matrix
---------------- | ----------------------
5V               | VCC
GND              | GND
D7 MOSI (GPIO13) | DIN
D8 CS (GPIO15)   | CS
D5 SCK (GPIO14)  | CLK

### For pyBoard

PyBoard | max7219 8x8 LED Matrix
------- | ----------------------
VIN     | VCC
GND     | GND
X8 MOSI | DIN
X5 CS   | CS
X6 SCK  | CLK

## Links

* Forked from [mcauser/micropython-max7219](https://github.com/mcauser/micropython-max7219)
* Based on [deshipu's max7219.py](https://bitbucket.org/thesheep/micropython-max7219/src)
* [micropython.org](http://micropython.org)
* [Docs on framebuf](http://docs.micropython.org/en/latest/pyboard/library/framebuf.html)
