#!/usr/bin/env python3

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import RPi.GPIO as GPIO

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('turn off the light')

    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(05,GPIO.OUT)

    while True: 
      print('press the button and speak')
      button.wait_for_press()
      print('eating pizza...')
      text = recognizer.recognize()
      if text is None:
        print('please repeat...')
      else:
        print('You said "', text, '"')
        if 'turn on the light' in text: 
          GPIO.output(05,GPIO.HIGH)
        elif 'turn off the light' in text:
          GPIO.output(05,GPIO.LOW)

if __name__ == '__main__':
    main()

