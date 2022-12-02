import cv2 as cv
import serial
from pyzbar.pyzbar import decode

class PiController():
    def __init__(self, Hui):
        self.HUI = Hui
        self.listening = False
        self.debug = True
        self.startMarker = '<'
        self.endMarker = '>'
        self.dataStarted = False
        self.dataBuf = ""
        self.messageComplete = False
        self.vid = cv.VideoCapture(0)
        self.serialPort = None
        self.__parse_file()
    
    def __parse_file(self):
        self.__setupSerial("9600","/dev/ttyACM0")
        
    def __setupSerial(self, baudRate, serialPortName):
        self.serialPort = serial.Serial(port= serialPortName, baudrate = baudRate, timeout=0, rtscts=True)

        print("Serial port " + serialPortName + " opened  Baudrate " + str(baudRate))
        self.__waitForArduino()

    def __sendToArduino(self, stringToSend):
        stringWithMarkers = (self.startMarker)
        stringWithMarkers += stringToSend
        stringWithMarkers += (self.endMarker)

        self.serialPort.write(stringWithMarkers.encode('utf-8')) # encode needed for Python3
       
    def __recvLikeArduino(self):
        if self.serialPort.inWaiting() > 0 and self.messageComplete == False or self.listening is True:
            x = self.serialPort.read().decode("utf-8", errors='replace') # decode needed for Python3
        
            if self.dataStarted == True:
                if x != self.endMarker:
                    self.dataBuf = self.dataBuf + x
                else:
                    self.dataStarted = False
                    self.messageComplete = True
            elif x == self.startMarker:
                self.dataBuf = ''
                self.dataStarted = True
    
        if (self.messageComplete == True):
            self.messageComplete = False
            return self.dataBuf
        else:
            return "XXX" 

    def __waitForArduino(self):
        print("Waiting for Arduino to reset")
     
        msg = ""
        while msg.find("Arduino is ready") == -1:
            msg = self.recvLikeArduino()
            if not (msg == 'XXX'): 
                print(msg)

    def __read_qr(self, frame):
        value = decode(frame)
        if len(value) == 0:
            return None

        return value[0].data.decode("utf-8") 

    def __scan_input(self):
        if self.debug:
            print("Camera On")
        while True:
            self.HUI.update()
            # if (self.HUI.mm_bool):
            #     return "Manual"
            
            ret, frame = self.vid.read()
            if ret == True:
                qr_value = self.__read_qr(frame)

            if qr_value is None: continue
            else: return qr_value

    def speak(self, qr_value):
        self.__sendToArduino(qr_value)

    def listen(self):
        while True:
            arduinoReply = self.__recvLikeArduino()
            if not (arduinoReply == 'XXX'):
                return arduinoReply
            self.HUI.update()   

    def see(self):
        self.__scan_input()  