from serial import Serial, SerialException

with Serial('/dev/cu.usbmodem84AC34F50B811', 9600) as ser:
    while True:
        print(ser.readline().decode())

