import datetime
import time
import keyboard
import cv2


def print_current_time():
    next_print_time = datetime.datetime.now() + datetime.timedelta(minutes=30)

    while True:
        current_time = datetime.datetime.now()

        if current_time >= next_print_time:
            print("Current time:", current_time.strftime("%H:%M:%S"))
            next_print_time = current_time + datetime.timedelta(minutes=30)

        if current_time.hour == 0 and current_time.minute == 0 and current_time.second == 0:
            print("The next day")
            break






        # Other code to be executed concurrently

        # Add a small delay to avoid high CPU usage
        time.sleep(1)


