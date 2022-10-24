from bs4 import BeautifulSoup
import urllib2
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT, initial=True)

if (sys.argv[1] == "off"):
        GPIO.cleanup()
        sys.exit()
else:
        direccion = "----"
        estado_critico = None
        estado_alto = None

        page = urllib2.urlopen(direccion).read()
        sopa = BeautifulSoup(page,"html.parser")
        estado_critico = sopa.find('span',class_="level_critico")
        estado_alto = sopa.find('span',class_="level_alto")

        if ((estado_critico != None) or (estado_alto != None)):
                GPIO.output(17, False)
        else:
                GPIO.cleanup()
