""" stub for Neopixel """
class NeoPixel:
    """ stub class """
    def __setitem__(self, index, val):
        pass

    def __getitem__(self, index):
        return (1, 1, 1)

    def fill(self, color):
        """ Colors all pixels the given ***color***. """

    def show(self):
        """ Shows the new colors on the pixels themselves if they haven't already
        been autowritten.

        The colors may or may not be showing after this function returns because
        it may be done asynchronously. """

    def clear(self):
        """ Clear all the pixels """
