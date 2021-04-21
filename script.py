import pyautogui
import time
import random
import sys







#   ███  █   █ █████  ███  █████ █   █ ████  █████ ████
#  █   █ █   █   █   █   █   █    █ █  █   █ █     █   █
#  █████ █   █   █   █   █   █     █   ████  ████  ████
#  █   █ █   █   █   █   █   █     █   █     █     █   █
#  █   █ █████   █    ███    █     █   █     █████ █   █
#                       by majd
# _________________________________________________________




# def script
def texxt(text):
    pyautogui.write(text)
    pyautogui.press('enter')


# code
count=0
pyautogui.FAILSAFE = True
text=input("what do you want the text to be?")

while True:
     try:
         tiime = int(input("how long should it take? (in seconds)"))
         break
     except ValueError:
         print("that wasn't a valid number.  try again.")

time.sleep(5)

try:

	while True:
		texxt()
		count+=1
		time.sleep(tiime)

except :

	print("finished and printed {} line(s)".format(count))
	#print("Unexpected error:", sys.exc_info()[0])
	exit()
