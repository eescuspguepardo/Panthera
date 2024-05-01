import serial
import time
arduinoData = serial.Serial("com3",115200)
time.sleep(1)
while True :
    while(neonviarduinoDataper.inWaiting()==0):
        pass
    dataPackat=arduinoData.readline()
    print(dataPackat)

# arduinoData = neonviper
# dataPackat = dadoemcasa
