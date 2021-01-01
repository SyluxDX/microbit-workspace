""" Micro:Bit stubs """
# pylint: disable=C0103, R0201

# Microbit core functions
def panic(value):
    """ Enter a panic mode. Requires restart.
    Pass in an arbitrary integer <= 255 to indicate a status """
    _ = value

def reset():
    """ Restart the board """

def sleep(milliseconds):
    """ Wait for n milliseconds. One second is 1000 milliseconds, so:

    microbit.sleep(1000)

    will pause the execution for one second. n can be an integer or a floating point number """
    _ = milliseconds
def running_time():
    """ Return the number of millisseconds since the board was switched on or restarted """
    return 1

def temperature():
    """ Return the temperature of the micro:bit in degrees Celcius """
    return 1

class accelerometer:
    """ Gives you access to the on-board accelerometer.
    The accelerometer also provides convenience functions for detecting gestures.
    By default MicroPython sets the accelerometer range to +/- 2g, changing the accelerometer range
    is currently not possible in MicroPython. The accelerometer returns a value in the range 0..1024
    for each axis, which is then scaled accordingly."""

    @classmethod
    def get_x(cls):
        """ Get the acceleration measurement in the x axis, as a positive or negative integer,
        depending on the direction. The measurement is given in milli-g. By default the
        accelerometer is configured with a range of +/- 2g, and so this method will return within
        the range of +/- 2000mg."""
        return 1

    @classmethod
    def get_y(cls):
        """ Get the acceleration measurement in the y axis, as a positive or negative integer,
        depending on the direction. The measurement is given in milli-g. By default the
        accelerometer is configured with a range of +/- 2g, and so this method will return within
        the range of +/- 2000mg."""
        return 1

    @classmethod
    def get_z(cls):
        """ Get the acceleration measurement in the z axis, as a positive or negative integer,
        depending on the direction. The measurement is given in milli-g. By default the
        accelerometer is configured with a range of +/- 2g, and so this method will return within
        the range of +/- 2000mg."""
        return 1

    @classmethod
    def get_values(cls):
        """ Get the acceleration measurements in all axes at once, as a three-element tuple of
        integers ordered as X, Y, Z. By default the accelerometer is configured with a range of +/-
        2g, and so X, Y, and Z will be within the range of +/-2000mg. """
        return (1, 1, 1)

    @classmethod
    def current_gesture(cls):
        """ Return the name of the current gesture. MicroPython understands the following gesture
        names:

        "up", "down", "left", "right", "face up", "face down", "freefall", "3g", "6g", "8g", "shake"

        Gestures are always represented as strings """
        return 'gesture'

    @classmethod
    def is_gesture(cls, name):
        """ Return True or False to indicate if the named gesture is currently active """
        _ = name
        return False

    @classmethod
    def was_gesture(cls, name):
        """ Return True or False to indicate if the named gesture was currently active """
        _ = name
        return False

    @classmethod
    def get_gestures(cls):
        """ Return a tuple of the gesture history. The most recent is listed last.
        Also clears the gesture history before returning """
        return ('up', 'up')

class _Button:
    """ Represents a button """
    def is_pressed(self):
        """ Returns True if the specified button button is currently being held down, and False
        otherwise """
        return True

    def was_pressed(self):
        """ Returns True or False to indicate if the button was pressed (went from up to down) since
        the device started or the last time this method was called. Calling this method will clear
        the press state so that the button must be pressed again before this method will return True
        again """
        return True

    def get_presses(self):
        """ Returns the running total of button presses, and resets this total to zero before
        returning """
        return 1
button_a = _Button()
button_b = _Button()

class compass:
    """ This module lets you access the built-in electronic compass. Before using, the compass
    should be calibrated, otherwise the readings may be wrong.

    Calibrating the compass will cause your program to pause until calibration is complete.
    Calibration consists of a little game to draw a circle on the LED display by rotating the
    device """

    @classmethod
    def calibrate(cls):
        """ Starts the calibration process. An instructive message will be scrolled to the user
        after which they will need to rotate the device in order to draw a circle on the LED
        display """
    @classmethod
    def is_calibrated(cls):
        """ Returns True if the compass has been successfully calibrated, and returns False
        otherwise """
        return True

    @classmethod
    def clear_calibration(cls):
        """ Undoes the calibration, making the compass uncalibrated again """

    @classmethod
    def get_x(cls):
        """ Gives the reading of the magnetic field strength on the x axis in nano tesla, as a
        positive or negative integer, depending on the direction of the field """
        return 1

    @classmethod
    def get_y(cls):
        """ Gives the reading of the magnetic field strength on the xy axis in nano tesla, as a
        positive or negative integer, depending on the direction of the field """
        return 1

    @classmethod
    def get_z(cls):
        """ Gives the reading of the magnetic field strength on the z axis in nano tesla, as a
        positive or negative integer, depending on the direction of the field """
        return 1

    @classmethod
    def heading(cls):
        """ Gives the compass heading, calculated from the above readings, as an integer in the
        range from 0 to 360, representing the angle in degrees, clockwise, with north as 0 """
        return 1

    @classmethod
    def get_field_strength(cls):
        """ Returns an integer indication of the magnitude of the magnetic field around the device
        in nano tesla """
        return 1

class display:
    """ This module controls the 5×5 LED display on the front of your board. It can be used to
    display images, animations and even text """

    @classmethod
    def get_pixel(cls, x, y):
        """ Return the brightness of the LED at column x and row y as an integer between 0 (off) and
        9 (bright) """
        _x = x
        _y = y
        return 1

    @classmethod
    def set_pixel(cls, x, y, value):
        """ Set the brightness of the LED at column x and row y to value, which has to be an integer
        between 0 and 9 """
        _x = x
        _y = y
        _v = value

    @classmethod
    def clear(cls):
        """ Set the brightness of all LEDs to 0 (off) """

    @classmethod
    def show(cls, value, delay=400, *, wait=True, loop=False, clear=False):
        """ Display the image

        If value is a string, float or integer, display letters/digits in sequence. Otherwise,
        if value is an iterable sequence of images, display these images in sequence. Each letter,
        digit or image is shown with delay milliseconds between them.

        If wait is True, this function will block until the animation is finished, otherwise the
        animation will happen in the background.

        If loop is True, the animation will repeat forever.

        If clear is True, the display will be cleared after the iterable has finished.

        Note that the wait, loop and clear arguments must be specified using their keyword """

    @classmethod
    def scroll(cls, value, delay=150, *, wait=True, loop=False, monospace=False):
        """ Scrolls value horizontally on the display. If value is an integer or float it is first
        converted to a string using str(). The delay parameter controls how fast the text is
        scrolling.

        If wait is True, this function will block until the animation is finished, otherwise the
        animation will happen in the background.

        If loop is True, the animation will repeat forever.

        If monospace is True, the characters will all take up 5 pixel-columns in width, otherwise
        there will be exactly 1 blank pixel-column between each character as they scroll.

        Note that the wait, loop and monospace arguments must be specified using their keyword """

    @classmethod
    def on(cls):
        """ Use to turn on the display """

    @classmethod
    def off(cls):
        """ Use to turn off the display (thus allowing you to re-use the GPIO pins associated with
        the display for other purposes) """

    @classmethod
    def is_on(cls):
        """ Returns True if the display is on, otherwise returns False """
        return True

    @classmethod
    def read_light_level(cls):
        """ Use the display’s LEDs in reverse-bias mode to sense the amount of light falling on the
        display. Returns an integer between 0 and 255 representing the light level, with larger
        meaning more light """
        return 1

class _MicroBitDigitalPin:
    """ Digital pin on the Micro:Bit board """

    def read_digital(self):
        """ Return 1 if the pin is high, and 0 if it's low """
        return 1

    def write_digital(self, value):
        """ Set the pin to High if the value is 1, or else set it to 0 """
        _ = value

class _MicroBitAnalogDigitalPin(_MicroBitDigitalPin):
    """Analog (PWM) pin on the Micro:Bit board """

    def read_analog(self):
        """ Reads the voltage applied to the pin, and return it as an integer between 0 (0V), and
        1024 (3.3V)"""
        return 1

    def write_analog(self, value):
        """ Output a PWM signal on the pin, with the duty cycle proportional to the provided value.
        The value may be either an integer or a floating point number between 0 (0% duty cycle) and
        1023 (100% duty) """
        _ = value


    def set_analog_period(self, period):
        """ Set the period of the PWM signal being output to period in milliseconds.
        The minimum valid value is 1ms. """
        _ = period


    def set_analog_period_microseconds(self,period):
        """ Set the period of the PWM signal being output to period in microseconds.
        The minimum valid value is 256µs. """
        _ = period

class _MicroBitTouchPin(_MicroBitAnalogDigitalPin):
    """ Touch sensitive pin on the Micro:Bit board """

    def is_touched(self):
        """ Return True if the pin is being touched with a finger, otherwise return False.

        This test is done by measuring how much resistance there is between the pin and ground.
        A low resistance gives a reading of True. To get a reliable reading using a finger you may
        need to touch the ground pin with another part of your body, for example your other hand """
        return True

pin0 = _MicroBitTouchPin()
pin1 = _MicroBitTouchPin()
pin2 = _MicroBitTouchPin()
pin3 = _MicroBitAnalogDigitalPin()
pin4 = _MicroBitAnalogDigitalPin()
pin5 = _MicroBitDigitalPin()
pin6 = _MicroBitDigitalPin()
pin7 = _MicroBitDigitalPin()
pin8 = _MicroBitDigitalPin()
pin9 = _MicroBitDigitalPin()
pin10 = _MicroBitAnalogDigitalPin()
pin11 = _MicroBitDigitalPin()
pin12 = _MicroBitAnalogDigitalPin()
pin13 = _MicroBitDigitalPin()
pin14 = _MicroBitDigitalPin()
pin15 = _MicroBitDigitalPin()
pin16 = _MicroBitDigitalPin()
pin19 = _MicroBitDigitalPin()
pin20 = _MicroBitDigitalPin()

class i2c:
    """ These module lets you communicate with devices connected to your board using the I²C bus
    protocol. There can be multiple slave devices connected at the same time, and each one has its
    own unique address, that is either fixed for the device or configured on it. Your board acts as
    the I²C master.

    We use 7-bit addressing for devices because of the reasons stated here.

    How exactly you should communicate with the devices, that is, what bytes to send and how to
    interpret the responses, depends on the device in question and should be described separately in
    that device’s documentation. """
    @classmethod
    def init(cls, freq=100000, sda=pin20, scl=pin19):
        """ Re-initialize peripheral with the specified clock frequency freq on the specified sda
        and scl pins.

        Warning: Changing the I²C pins from defaults will make the accelerometer and compass stop
        working, as they are connected internally to those pins """

    @classmethod
    def read(cls, addr, n, repeat=False):
        """ Read n bytes from the device with 7-bit address addr. If repeat is True, no stop bit
        will be sent """
        _a = addr
        _n = n
        _r = repeat
        return b'\x00\x01'

    @classmethod
    def write(cls, addr, buf, repeat=False):
        """ Write bytes from buf to the device with 7-bit address addr. If repeat is True, no stop
        bit will be sent """

class Image:
    """ Used to create images that can be displayed easily on the device’s LED matrix. Given an
    image object it’s possible to display it via the display API. There are four ways in which you
    can construct an image:

    Image() - Create a blank 5x5 image

    Image(string) - Create an image by parsing the string, a single character returns that glyph

    Image(width, height) - Create a blank image of given size

    Image(width, height, buffer) - Create an image from the given buffer

    Note: __init__'s docstring have more info """

    def __init__(self, *args, **kwargs):
        """ If string is used, it has to consist of digits 0-9 arranged into lines, describing the
        image, for example:

        image = Image("90009:""09090:""00900:""09090:""90009")

        will create a 5×5 image of an X. The end of a line is indicated by a colon. It’s also
        possible to use a newline (n) to indicate the end of a line.

        The other form creates an empty image with width columns and height rows. Optionally buffer
        can be an array of width x height integers in range 0-9 to initialize the image:

        Image(2, 2, b'\\x08\\x08\\x08\\x08')

        or:

        Image(2, 2, bytearray([9,9,9,9]))

        Will create a 2 x 2 pixel image at full brightness """

    def width(self):
        """ Return the number of columns in the image """
        return 1

    def height(self):
        """ Return the numbers of rows in the image """
        return 1

    def set_pixel(self, x, y, value):
        """ Set the brightness of the pixel at column x and row y to the value, which has to be
        between 0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in read-only images,
        like Image.HEART """
        _x = x
        _y = y
        _v = value

    def get_pixel(self, x, y):
        """ Return the brightness of pixel at column x and row y as an integer between 0 and 9 """
        _x = x
        _y = y
        return 1

    def shift_left(self, n):
        """ Return a new image created by shifting the picture left by n columns """
        _ = n

    def shift_right(self, n):
        """ Same as image.shift_left(-n) """
        _ = n

    def shift_up(self, n):
        """ Return a new image created by shifting the picture up by n rows """
        _ = n

    def shift_down(self, n):
        """ Same as image.shift_up(-n) """
        _ = n

    def crop(self, x, y, w, h):
        """ Return a new image by cropping the picture to a width of w and a height of h, starting
        with the pixel at column x and row y """
        _x = x
        _y = y
        _w = w
        _h = h

    def copy(self):
        """ Return an exact copy of the image """
        return Image()

    def invert(self):
        """ Return a new image by inverting the brightness of the pixels in the source image """
        return Image()

    def fill(self, value):
        """ Set the brightness of all the pixels in the image to the value, which has to be between
        0 (dark) and 9 (bright).

        This method will raise an exception when called on any of the built-in read-only images,
        like Image.HEART """

    def blit(self, src, x, y, w, h, xdest=0, ydest=0):
        """ Copy the rectangle defined by x, y, w, h from the image src into this image at xdest,
        ydest. Areas in the source rectangle, but outside the source image are treated as having a
        value of 0 """
    HEART = Image()
    HEART_SMALL = Image()
    HAPPY = Image()
    SMILE = Image()
    SAD = Image()
    CONFUSED = Image()
    ANGRY = Image()
    ASLEEP = Image()
    SURPRISED = Image()
    SILLY = Image()
    FABULOUS = Image()
    MEH = Image()
    YES = Image()
    NO = Image()
    CLOCK12 = Image()
    CLOCK11 = Image()
    CLOCK10 = Image()
    CLOCK9 = Image()
    CLOCK8 = Image()
    CLOCK7 = Image()
    CLOCK6 = Image()
    CLOCK5 = Image()
    CLOCK4 = Image()
    CLOCK3 = Image()
    CLOCK2 = Image()
    CLOCK1 = Image()
    ARROW_N = Image()
    ARROW_NE = Image()
    ARROW_E = Image()
    ARROW_SE = Image()
    ARROW_S = Image()
    ARROW_SW = Image()
    ARROW_W = Image()
    ARROW_NW = Image()
    TRIANGLE = Image()
    TRIANGLE_LEFT = Image()
    CHESSBOARD = Image()
    DIAMOND = Image()
    DIAMOND_SMALL = Image()
    SQUARE = Image()
    SQUARE_SMALL = Image()
    RABBIT = Image()
    COW = Image()
    MUSIC_CROTCHET = Image()
    MUSIC_QUAVER = Image()
    MUSIC_QUAVERS = Image()
    PITCHFORK = Image()
    XMAS = Image()
    PACMAN = Image()
    TARGET = Image()
    TSHIRT = Image()
    ROLLERSKATE = Image()
    DUCK = Image()
    HOUSE = Image()
    TORTOISE = Image()
    BUTTERFLY = Image()
    STICKFIGURE = Image()
    GHOST = Image()
    SWORD = Image()
    GIRAFFE = Image()
    SKULL = Image()
    UMBRELLA = Image()
    SNAKE = Image()

class spi:
    """ The spi module lets you talk to a device connected to your board using a serial peripheral
    interface (SPI) bus. SPI uses a so-called master-slave architecture with a single master. You
    will need to specify the connections for three signals:

    SCLK : Serial Clock (output from master).

    MOSI : Master Output, Slave Input (output from master).

    MISO : Master Input, Slave Output (output from slave) """

    @classmethod
    def init(cls, baudrate=1000000, bits=8, mode=0, sclk=pin13, mosi=pin15, miso=pin14):
        """ Initialize SPI communication with the specified parameters on the specified pins. Note
        that for correct communication, the parameters have to be the same on both communicating
        devices.

        The baudrate defines the speed of communication.

        The bits defines the size of bytes being transmitted. Currently only bits=8 is supported.
        However, this may change in the future.

        The mode determines the combination of clock polarity and phase according to the following
        convention, with polarity as the high order bit and phase as the low order bit:

        SPI Mode 	Polarity (CPOL) 	Phase (CPHA)
        0 	0 	0

        1 	0 	1

        2 	1 	0

        3 	1 	1

        Polarity (aka CPOL) 0 means that the clock is at logic value 0 when idle and goes high
        (logic value 1) when active; polarity 1 means the clock is at logic value 1 when idle and
        goes low (logic value 0) when active. Phase (aka CPHA) 0 means that data is sampled on the
        leading edge of the clock, and 1 means on the trailing edge """

    @classmethod
    def read(cls, nbytes):
        """ Read at most nbytes. Returns what was read """
        _ = nbytes
        return b'\x00\x00'

    @classmethod
    def write(cls, buffer):
        """ Write the buffer of bytes to the bus """

    @classmethod
    def write_readinto(cls, out_buffer, in_buffer):
        """ Write the out_buffer to the bus and read any response into the in_buffer. The length of
        the buffers should be the same. The buffers can be the same object """

class uart:
    """ The uart module lets you talk to a device connected to your board using a serial
    interface """

    @classmethod
    def init(cls, baudrate=9600, bits=8, parity=None, stop=1, *, tx=None, rx=None):
        """ Initialize serial communication with the specified parameters on the specified tx and rx
        pins. Note that for correct communication, the parameters have to be the same on both
        communicating devices.

        Warning: Initializing the UART on external pins will cause the Python console on USB to
        become unaccessible, as it uses the same hardware. To bring the console back you must
        reinitialize the UART without passing anything for tx or rx (or passing None to these
        arguments). This means that calling uart.init(115200) is enough to restore the Python
        console.

        The baudrate defines the speed of communication. Common baud rates include:

        9600, 14400, 19200, 28800, 38400, 57600, 115200

        The bits defines the size of bytes being transmitted, and the board only supports 8. The
        parity parameter defines how parity is checked, and it can be None, microbit.uart.ODD or
        microbit.uart.EVEN. The stop parameter tells the number of stop bits, and has to be 1 for
        this board.

        If tx and rx are not specified then the internal USB-UART TX/RX pins are used which connect
        to the USB serial converter on the micro:bit, thus connecting the UART to your PC. You can
        specify any other pins you want by passing the desired pin objects to the tx and rx
        parameters.

        Note: When connecting the device, make sure you “cross” the wires – the TX pin on your board
        needs to be connected with the RX pin on the device, and the RX pin – with the TX pin on the
        device. Also make sure the ground pins of both devices are connected """

    @classmethod
    def any(cls):
        """ Return True if any data is waiting, else False """
        return True

    @classmethod
    def read(cls, nbytes=None):
        """ Read bytes. If nbytes is specified then read at most that many bytes, otherwise read as
        many bytes as possible. Return value: a bytes object or None on timeout.

        A bytes object contains a sequence of bytes. Because ASCII characters can fit in single
        bytes this type of object is often used to represent simple text and offers methods to
        manipulate it as such, e.g. you can display the text using the print() function.

        You can also convert this object into a string object, and if there are non-ASCII characters
        present the encoding can be specified:

        msg_bytes = uart.read()

        msg_str = str(msg, 'UTF-8') """

    @classmethod
    def readinto(cls, buffer, nbytes=None):
        """ Read bytes into the buf. If nbytes is specified then read at most that many bytes.
        Otherwise, read at most len(buf) bytes. Return value: number of bytes read and stored into
        buf or None on timeout """
        _b = buffer
        _n = nbytes
        return b'\x00\x00'

    @classmethod
    def readline(cls):
        """ Read a line, ending in a newline character. Return value: the line read or None on
        timeout. The newline character is included in the returned bytes """
        return ''

    @classmethod
    def write(cls, buf):
        """ Write the buffer to the bus, it can be a bytes object or a string:

        uart.write('hello world')

        uart.write(b'hello world')

        uart.write(bytes([1, 2, 3]))

        Return value: number of bytes written or None on timeout """
