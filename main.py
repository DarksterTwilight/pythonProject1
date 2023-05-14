import threading
import datetime
import time
import audio_Recodring_test
import speech_to_text
import chatgpt_responce
# import date_time_print_trial
import text_to_speech



def system_response():
    while True:
        user_input = input('Enter 1 to start recoding')
        if user_input == '1':
            audio_Recodring_test.record_audio()
            text = speech_to_text.transcribe_audio_to_text('recording.wav') + ". CURRENT TIME : " + datetime.datetime.now().strftime("%H:%M:%S")
            print('Your Prompt is :  \n'+ text)
            chat_transcript = chatgpt_responce.gtp_responce(text)
            print(chat_transcript[0] + "\n")
            assistant_responce = chat_transcript[1]
            text_to_speech.text_to_speech(assistant_responce)
        else:
            print('Invalid Input try again......')

def print_current_time():
    next_print_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
    print('CURRENT TIME : '+ datetime.datetime.now().strftime("%H:%M:%S"))

    while True:
        current_time = datetime.datetime.now()

        if current_time >= next_print_time:
            Time_update  = "CURRENT TIME : " + current_time.strftime("%H:%M:%S")
            print(Time_update)
            next_print_time = current_time + datetime.timedelta(minutes=30)
            chat_transcript = chatgpt_responce.gtp_responce(Time_update)
            print(chat_transcript + '\n')


        if current_time.hour == 8 and current_time.minute == 0 and current_time.second == 0:
            Day_time_update = "TOMORROW BEGINS. CURRENT TIME : " + current_time.strftime("%H:%M:%S")
            print(Day_time_update)
            chat_transcript = chatgpt_responce.gtp_responce(Day_time_update)
            print(chat_transcript+ '\n')

        # Add a small delay to avoid high CPU usage
        # sleep for 25 min
        time.sleep(1500)



# Create threads for each function
time_thread = threading.Thread(target= print_current_time)

response_thread = threading.Thread(target= system_response)


# Start the threads
time_thread.start()
response_thread.start()

# Join the threads (optional)
time_thread.join()
response_thread.join()



