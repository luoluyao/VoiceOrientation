import time
from pixels import Pixels, pixels
#from alexa_led_pattern import AlexaLedPattern
from google_home_led_pattern import GoogleHomeLedPattern

if __name__ == '__main__':

    pixels.pattern = GoogleHomeLedPattern(show=pixels.show, color=2)

    while True:

        try:
            #pixels.wakeup()
            #time.sleep(3)
            #pixels.think()
            #time.sleep(3)
            pixels.speak()
            time.sleep(6)
            #pixels.off()
            #time.sleep(3)
        except KeyboardInterrupt:
            break


    pixels.off()
    time.sleep(1)
