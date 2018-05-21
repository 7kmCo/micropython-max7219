# MicroPython MAX7219 8x8 LED Matrix

A MicroPython library for the MAX7219 8x8 LED matrix driver, SPI interface, supports cascading and uses [framebuf](http://docs.micropython.org/en/latest/pyboard/library/framebuf.html)


## How to use

```
import matrix
matrix = matrix.Matrix()
```

At the moment, only three methods (text, scroll and shape) added to the `Matrix` class whitch samples can be found in `/examples` directory, more will be added later. Fill free to make suggestions, pull requests are wellcome.

```matrix.text(txt = 'F', x = 0, y = 0, c = 1)```

which x is horizontal offset default is zero, y is vertical offset default is zero and c is color default is 1.

```matrix.scroll(txt = 'Scrolling text example', s = 0.1, c = 1)```

which x, y and c as aboce and s is speed of scrolling default is 0.1 second.

```
shape = [[0,0,0,0,0,0,0,0], [0,1,1,0,0,1,1,0], [1,0,0,1,1,0,0,1], [1,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,1], [0,1,0,0,0,0,1,0], [0,0,1,0,0,1,0,0], [0,0,0,1,1,0,0,0]]
matrix.shape(patern = shape, delay = 0)
```

which shape is an array of values zero or one values for each pixel. the aboce shape, will display a heart. 

The default value for delay (not the best name, but this was the best I found!) is zero. If zero, it just display the shape, but if is set to some values, led matrix will start to display the shape one pixel (In our case, one led) at a time by the interval amount set for delay variable.


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
