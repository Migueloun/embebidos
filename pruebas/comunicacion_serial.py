import serial

arduino = serial.Serial("/dev/ttyACM0", baudrate=9600,timeout=3.0)

while True:
    sensor_nivel = arduino.readline()
    print(sensor_nivel)

arduino.close()