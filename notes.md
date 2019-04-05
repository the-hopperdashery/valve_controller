ch340g - usb chip

import serial
ser = serial.Serial('/dev/tty.usbserial-1410')
print(ser.name)         # check which port was really used
ser.write(b'\x3A\x46\x45\x30\x35\x30\x30\x30\x37\x46\x46\x30\x30\x46\x37\x0D\x0A')
ser.write(b'\x3A\x46\x45\x30\x35\x30\x30\x30\x37\x46\x46\x30\x30\x46\x37\x0D\x0A')     # write a string
ser.close()

# Overview:

## Pages
### Water Valves
 - 3 valves
 - need manual on/off buttons
 - runtime input
 - offtime input
 - 2:1 ratio of relays to valves

### Climate
 - 3 of these
 - light timer style (turn on 7 am and run for x hrs)

### Lighting
 - purpose: day extension
 - subtract 30 from sunset and turn on the lights for x hours