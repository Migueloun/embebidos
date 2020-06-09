import wiringpi as wiringpi

wiringpi.wiringPiSetup();

wiringpi.pinMode(4, 0)
wiringpi.pinMode(0, 1)


while True:
    sensor = wiringpi.digitalRead(4)
    if (sensor == 0):
        wiringpi.digitalWrite(0,1)
    else:
        wiringpi.digitalWrite(0,0)

