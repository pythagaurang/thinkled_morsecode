from time import sleep
import os

morsedict={ 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 
        'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 
        'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 
        'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
        '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-','\'':'.----.',' ':'/'
}

#multiplier for sleep time, change this if you want to personalise your morse language
multipliers={
    'dot':1,
    'dash':3,
    'innerchar_gap':1,
    'short_gap':3,
    'medium_gap':6
}

#change this string to whatever you want to transmit using morse code, make sure you don't use characters from outside of above dict.
inputstring="Save Me"

#unit_time is the amount of time in seconds for dot and intrachar_gap
unit_time=0.05

#change the letter a to 0 for transmitting through power button
ledon =b"\x8a"
ledoff=b"\x0a"

def encryptor(a):
    b=''
    for letter in a:
        c=morsedict[letter]+' '
        b+=c
    return b

def morse_led(string):
    for code in string:
        if(code=='.'):
            led(True)
            sleep(unit_time*multipliers['dot'])
            led(False)
            sleep(unit_time*multipliers['innerchar_gap'])
        elif(code=='-'):
            led(True)
            sleep(unit_time*multipliers['dash'])
            led(False)
            sleep(unit_time*multipliers['innerchar_gap'])
        elif(code==' '):
            led(False)
            sleep(unit_time*multipliers['short_gap'])            
        elif(code=='/'):
            led(False)
            sleep(unit_time*multipliers['medium_gap'])

def led(state):
    if state:
        led = open("/sys/kernel/debug/ec/ec0/io", "wb")
        led.seek(12)
        led.write(ledon)
        led.flush()
    else:
        led = open("/sys/kernel/debug/ec/ec0/io", "wb")
        led.seek(12)
        led.write(ledoff)
        led.flush()

morsestring=encryptor(inputstring.lower())
def morse_loop():
    while True:
        sleep(1)
        morse_led(morsestring)

if __name__ == '__main__':
    try:
        morse_loop(morsestring)
    except KeyboardInterrupt:
        if(input("\nInterrupted: Turn off led?(y/n) ").lower()=="y"):
            led(False)
        else:
            led(True)
