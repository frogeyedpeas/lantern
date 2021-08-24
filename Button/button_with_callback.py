import RPi.GPIO as GPIO  


#sample code from here: https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
#fuck that use this instead: https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/


BUTTON_GPIO = 21 

def button_pressed_callback(channel):
    print("Button pressed!")

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)  

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=100)

    i = 0
    while True:
        i+=1
