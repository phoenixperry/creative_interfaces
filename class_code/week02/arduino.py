#!/Applications/Python_2_7
import serial
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
while True: 
		print ser.readline() 
