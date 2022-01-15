import RPi.GPIO as GPIO 
from datetime import datetime 

btnLoop1 = 8
btnTicket = 10
btnLoop2 = 12

#GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(btnLoop1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(btnTicket, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(btnLoop2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

def btnLoop1_callback(channel):
    print("btnLoop1 was pushed! ",datetime.now())
    detectCarLoop1()

def ticket_callback(channel):
    print("btnTicket was pushed! ",datetime.now())
    printTicket()

def btnLoop2_callback(channel):
    print("btnLoop2 was pushed! ",datetime.now())
    detectCarLoop2()

def detectCarLoop1():
    print("Selamat Datang")

def printTicket():
    print("Cetak Tiket Masuk")

def detectCarLoop2():
    print("Terimakasih")

GPIO.add_event_detect(btnLoop1,GPIO.RISING,callback=btnLoop1_callback, bouncetime=500) 
GPIO.add_event_detect(btnTicket,GPIO.RISING,callback=ticket_callback, bouncetime=500) 
GPIO.add_event_detect(btnLoop2,GPIO.RISING,callback=btnLoop2_callback, bouncetime=500) 

message = input("Press enter to quit\n\n") 
GPIO.cleanup() 
