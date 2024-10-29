from serial import Serial, SerialException

# with Serial('/dev/cu.usbmodem84AC34F50B811', 9600) as ser:
#     while True:
#         print(ser.readline().decode())

####################

# with Serial('/dev/cu.usbmodem84AC34F50B811', 9600) as ser:
#     ser.write(bytes([0x1]))
#     input() # keep port open to see the LED turn on

####################

# with Serial('/dev/cu.usbmodem84AC34F50B811', 9600) as ser:
#     ser.write(bytes([0x1]))
#     assert ser.read() == bytes([0xaa])# ASSERTION ERROR HERE

#     ser.write(bytes([0x0]))
#     assert ser.read() == bytes([0xaa])# ASSERTION ERROR HERE

#     ser.write(bytes([0x2]))
#     assert ser.read() == bytes([0xff])# ASSERTION ERROR HERE



import tkinter as tk
import tkinter.ttk as ttk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LED Blinker")

if __name__ == '__main__':
    app = App()
    app.mainloop()


def __init__(self):
    super().__init__()
    self.title("LED Blinker")
    ttk.Checkbutton(self, text='Toggle LED').pack()
    ttk.Button(self, text='Send Invalid').pack()
    ttk.Button(self, text='Disconnect', default='active').pack()






