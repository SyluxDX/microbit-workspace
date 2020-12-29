""" This module allows you play sounds from a speaker attached to the Microbit. In order to use the
audio module you will need to provide a sound source.

A sound source is an iterable (sequence, like list or tuple, or a generator) of frames, each of 32
samples. The audio modules plays samples at the rate of 7812.5 samples per second, which means that
it can reproduce frequencies up to 3.9kHz """
import microbit

def play(source, wait=True, pin=microbit.pin0, return_pin=None):
    """ Play the source to completion.

    source is an iterable, each element of which must be an AudioFrame.

    If wait is True, this function will block until the source is exhausted.

    pin specifies which pin the speaker is connected to.

    return_pin specifies a differential pin to connect to the speaker instead of ground """
    _s = source
    _w = wait
    _p = pin
    _r = return_pin
class AudioFrame:
    """ An AudioFrame object is a list of 32 samples each of which is a signed byte (whole number
    between -128 and 127). It takes just over 4 ms to play a single frame """
