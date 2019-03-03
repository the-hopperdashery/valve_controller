import serial

COMMANDS = [
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x30\x46\x46\x30\x30\x46\x45\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x30\x30\x30\x30\x30\x46\x44\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x31\x46\x46\x30\x30\x46\x44\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x31\x30\x30\x30\x30\x46\x43\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x32\x46\x46\x30\x30\x46\x43\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x32\x30\x30\x30\x30\x46\x42\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x33\x46\x46\x30\x30\x46\x42\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x33\x30\x30\x30\x30\x46\x41\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x34\x46\x46\x30\x30\x46\x41\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x34\x30\x30\x30\x30\x46\x39\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x35\x46\x46\x30\x30\x46\x39\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x35\x30\x30\x30\x30\x46\x38\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x36\x46\x46\x30\x30\x46\x38\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x36\x30\x30\x30\x30\x46\x37\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x37\x46\x46\x30\x30\x46\x37\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x37\x30\x30\x30\x30\x46\x36\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x38\x46\x46\x30\x30\x46\x36\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x38\x30\x30\x30\x30\x46\x35\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x39\x46\x46\x30\x30\x46\x35\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x39\x30\x30\x30\x30\x46\x34\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x41\x46\x46\x30\x30\x46\x34\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x41\x30\x30\x30\x30\x46\x33\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x42\x46\x46\x30\x30\x46\x33\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x42\x30\x30\x30\x30\x46\x32\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x43\x46\x46\x30\x30\x46\x32\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x43\x30\x30\x30\x30\x46\x31\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x44\x46\x46\x30\x30\x46\x31\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x44\x30\x30\x30\x30\x46\x30\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x45\x46\x46\x30\x30\x46\x30\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x45\x30\x30\x30\x30\x46\x46\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x46\x46\x46\x30\x30\x46\x46\x0D\x0A',
    b'\x3A\x46\x45\x30\x35\x30\x30\x30\x46\x30\x30\x30\x30\x46\x45\x0D\x0A',
]

class Board:
    def __init__(self):
        self.ser = serial.Serial('/dev/tty.usbserial-1410')
        print(self.ser.name)         # check which port was really used

    def on(self, relay_number):
        self.ser.write(self.command_finder(relay_number, 'on'))

    def off(self, relay_number):
        self.ser.write(self.command_finder(relay_number, 'off'))

    def command_finder(self, relay_number, state):
        # on command index
        idx = (relay_number - 1) * 2

        if state == 'off':
            idx = idx + 1
        print(idx)

        return COMMANDS[idx]

print('hi')
