
import socket
import csv

import smtplib

def email():
    print("person fall notification sending...")
    content = 'Help me out!'

    mail = smtplib.SMTP('smtp.gmail.com',587)

    mail.ehlo() # ehlo is a standard smtp server;

    mail.starttls()

    mail.login('chhamadhawan@gmail.com', 'Kshama@71')

    mail.sendmail('chhamadhawan@gmail.com','charchitdhawan@gmail.com', content)

    mail.quit()

    
UDP_IP = ""
UDP_PORT = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    raw=str(data)
    #print (raw)
    raw=raw.split(',')
    #print (raw)
    #raw=list(map(split("'"),raw))
    #print(raw)
    x=float(raw[2])
    print("\nAcceleration: ",x)
    
    y=float(raw[3])
    print("\nGyroscope: ",y)
    z=raw[4][:len(raw[4])-1]
    z=float(z)
    # print(z)
    
    
    if int(x) > 3  and int(y) > 3:
        email()
    else:
        print("condition is ok...")
