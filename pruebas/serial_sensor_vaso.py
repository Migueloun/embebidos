import serial
import wiringpi as wiringpi

wiringpi.wiringPiSetup();
wiringpi.pinMode(4, 0)
wiringpi.pinMode(0, 1)

arduino = serial.Serial("/dev/ttyACM0", baudrate=9600,timeout=3.0)

while True:
    sensor_nivel = arduino.readline()
    sensor = wiringpi.digitalRead(4)
    if (sensor == 0):
        wiringpi.digitalWrite(0,1)
    else:
        wiringpi.digitalWrite(0,0)
        
    print(sensor_nivel)
    
arduino.close()