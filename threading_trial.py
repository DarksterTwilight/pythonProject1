import threading
import time
import datetime


def update_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("CURRENT TIME:", current_time)
        time.sleep(1800)  # Sleep for half an hour (1800 seconds)


def system_response2():
    while True:
        user_input = input()
        if user_input.lower() == "hi":
            print("Hi Master")


def print_current_time2():
    next_print_time = datetime.datetime.now() + datetime.timedelta(seconds=5)

    while True:
        current_time = datetime.datetime.now()

        if current_time >= next_print_time:
            Time_update = "CURRENT TIME : " + current_time.strftime("%H:%M:%S")
            print(Time_update)
            next_print_time = current_time + datetime.timedelta(seconds=5)
            # chat_transcript = chatgpt_responce.gtp_responce(Time_update)
            # print(chat_transcript + '\n')

        if current_time.hour == 8 and current_time.minute == 27 and current_time.second == 5:
            Day_time_update = "TOMORROW BEGINS. CURRENT TIME : " + current_time.strftime("%H:%M:%S")
            print(Day_time_update)
            # chat_transcript = chatgpt_responce.gtp_responce(Day_time_update)
            # print(chat_transcript+ '\n')

        # Add a small delay to avoid high CPU usage
        time.sleep(3)


# Create threads for each function
time_thread = threading.Thread(target=print_current_time2)
response_thread = threading.Thread(target=system_response2)

# Start the threads
time_thread.start()
response_thread.start()

# Join the threads (optional)
time_thread.join()
response_thread.join()
