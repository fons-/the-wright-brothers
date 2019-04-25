import onionGpio
import time
import sys

g = onionGpio.OnionGpio(11)
g.setOutputDirection(0)

unit_length = .1

lampaan = lambda: g.setValue(0)
lampuit = lambda: g.setValue(1)

#lampaan = lambda: print("1")
#lampuit = lambda: print("0")

# From https://www.geeksforgeeks.org/morse-code-translator-python/
# by Palash Nigam
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':' '}


def beep(num_units):
    lampaan()
    time.sleep(unit_length*num_units)
    lampuit()


def pause(num_units):
    time.sleep(unit_length*num_units)


def play_letter(letter):
    for morse_symbol in MORSE_CODE_DICT[letter]:
        if morse_symbol == '.':
            beep(1)
        elif morse_symbol == '-':
            beep(3)
        elif morse_symbol == ' ':
            pause(1)
        pause(1)


def play_text(text):
    text = [c for c in str.upper(text) if c in MORSE_CODE_DICT]
    for letter in text:
        play_letter(letter)
        pause(3-1)


if __name__ == "__main__":
    for line in sys.stdin:
        play_text(line)
