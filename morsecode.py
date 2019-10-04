from time import sleep

morsedict={ 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 
        'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 
        'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 
        'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
        '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-',' ':'w'
}

multipliers={
    'dot':1,
    'dash':3,
    'innerchar_gap':1,
    'short_gap':1,
    'medium_gap':7
}

inputstring="Save Me"
unit_time=0.3


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
        elif(code=='w'):
            led(False)
            sleep(unit_time*multipliers['short_gap'])            
        elif(code==' '):
            led(False)
            sleep(unit_time*multipliers['medium_gap'])

def led(state):
    if state:
        led = open("/sys/kernel/debug/ec/ec0/io", "wb")
        led.seek(12)
        led.write(b"\x8a")
        led.flush()
    else:
        led = open("/sys/kernel/debug/ec/ec0/io", "wb")
        led.seek(12)
        led.write(b"\x0a")
        led.flush()

morsestring=encryptor(inputstring.lower())
while True:
    morse_led(morsestring)
