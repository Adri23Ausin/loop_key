import sys
import time

import pyautogui

if __name__ == '__main__':

    # Defaults
    key = "space"
    seconds = 30 * 60  # 30 mins * 60 secs/min

    # List of numbers from 0 to 9 in str
    numbers = [str(x) for x in range(0, 10)]

    # If there are more arguments than needed --> Exit program
    if len(sys.argv) > 3:
        print("ERROR. More arguments than needed. Max == 3. loop_key.exe | (Minutes) | (Key Pressed)")
        sys.exit(1)

    # Change defaults variables according to arguments passed
    for index, item in enumerate(sys.argv):
        if index == 0:  # Python file
            continue
        if item[0] in numbers:
            seconds = int(item) * 60
        else:
            key = item

    print("Program will execute for {} seconds = {} mins".format(seconds, int(seconds / 60)))
    print(f"Key *{key}* will be pressed")
    print("5 seconds of courtesy...")
    time.sleep(5)
    while seconds > 0:
        pyautogui.press(key)
        time.sleep(1)
        print(f"{(int(seconds / 60))} mins and {(seconds % 60)} seconds left")
        seconds -= 1
