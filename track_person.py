import subprocess
import pyttsx3
import time
tts = pyttsx3.init()

#replace ip address with the allocated ip for device to be tracked
my_ip= "192.168.**.**"

c = 0

while True: 
    pingip = subprocess.Popen(['ping' , my_ip] , stdout=subprocess.PIPE)
    time.sleep(4)
    if(pingip.poll() == 0 ):
        if c == 0:
            tts.say(x + " just connected to the internet!")
            tts.runAndWait()
        c = 1
        print("user is connected")
    else:
        if c == 1:
            tts.say(x + " just disconnected from the internet!")
            tts.runAndWait()
        c = 0
        print("user is disconnected")
