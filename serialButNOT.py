from serial import Serial, SerialException

# with Serial('/dev/cu.usbmodem84AC34F50B81', 9600) as ser:
#     while True:
#         print(ser.readline().decode())

with Serial('/dev/cu.usbmodem84AC34F50B811', 9600) as ser:
    ser.write(bytes([0x0]))
    input() # keep port open to see the LED turn on


# with Serial('/dev/cu.usbmodem84AC34F50B81', 9600) as ser:
#     ser.write(bytes([0x1]))
#     assert ser.read() == bytes([0xaa])

#     ser.write(bytes([0x0]))
#     assert ser.read() == bytes([0xaa])

#     ser.write(bytes([0x2]))
#     assert ser.read() == bytes([0xff])