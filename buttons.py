import time
import os
import board
import digitalio

print("press a button!")

button1 = digitalio.DigitalInOut(board.D2)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

button2 = digitalio.DigitalInOut(board.D3)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(board.D17)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

button4 = digitalio.DigitalInOut(board.D27)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.DOWN

button5 = digitalio.DigitalInOut(board.D23)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.DOWN

button6 = digitalio.DigitalInOut(board.D13)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.DOWN

button7 = digitalio.DigitalInOut(board.D19)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.DOWN

button8 = digitalio.DigitalInOut(board.D26)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.DOWN

while True:

    # omxplayer -o local <file>
    # omxplayer -o hdmi <file>
    # omxplayer -o both <file>
    if button1.value:
        print("Button 1 pressed!")
        # os.system('omxplayer audio/gluszec.wav &')

    if button2.value:
        print("Button 2 pressed!")
        # os.system('omxplayer audio/jelen.wav &')

    if button3.value:
        print("Button 3 pressed!")
        # os.system('omxplayer audio/nietoperze.wav &')

    if button4.value:
        print("Button 4 pressed!")
        # os.system('omxplayer audio/orzel.wav &')

    if button5.value:
        print("Button 5 pressed!")
        # os.system('omxplayer audio/pszczoly.wav &')

    if button6.value:
        print("Button 6 pressed!")
        # os.system('omxplayer audio/sowa.wav &')

    if button7.value:
        print("Button 7 pressed!")
        # os.system('omxplayer audio/wilk.wav &')

    if button8.value:
        print("Button 8 pressed!")
        # os.system('omxplayer audio/zaby.wav &')

    time.sleep(.25)