""" script """
import argparse
import microfs

MAIN = ''
ADDONS = []

def clear_microbit():
    """ clear files from micro:bit """
    print('Cleaning micro:bit file system')
    files = microfs.ls()
    for fname in files:
        microfs.rm(fname)

def flash():
    """ flash files to micro:bit """
    # Copy additional scripts
    if len(ADDONS) > 0:
        print('Copying additional scripts')
        for name in ADDONS:
            print(' ', name)
            microfs.put(name)
    print('Copying main script: ', MAIN)
    microfs.put(MAIN, 'main.py')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Flash main and additional python scripts to micro:bit')
    parser.add_argument('-c', '--clear', action='store_true',
        help='Remove files from microbot before flashing')
    ARGS = parser.parse_args()

    if ARGS.clear:
        clear_microbit()
    flash()
