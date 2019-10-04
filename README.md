# thinkled_morsecode

Inspired from that reddit [post](https://redd.it/dcay0w).

I wrote a morse translator first that'd just translate English letters to morse code. Then I wrote a function to display the morse code. For all this I reffered [the morse wiki](https://en.wikipedia.org/wiki/Morse_code).

For the led on and off code, I reffered this reddit [post](https://redd.it/7n8eyu/).

## Getting Started
- Run the following commands in terminal or add `ec_sys.write_support=1` to your kernel parameters.
```
sudo modprobe -r ec_sys
sudo modprobe ec_sys write_support=1
```
- Clone this repository and run the python file as root.
```
sudo python3 thinkled_morsecode/morsecode.py
```
