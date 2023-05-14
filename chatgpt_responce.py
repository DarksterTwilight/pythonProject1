import openai, subprocess

openai.api_key = "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"

messages = [{"role": "system", "content": 'You are my personal assistant who will create a time table(from 9:00 AM to 10:00 PM) based on the to-do list that user provides. You will ask for constant feedback form user in order to update and improve the time-table, when the time-table has been approved by the user, remember the time-table and assist the user however he asks. Whenever user provides you with the CURRENT TIME(in the format of H:M:S), you would tell him the task asper time table that he needs to do and would also ask weather he has already done it or not. If he has not started/ done it, encourage him to do the task or of he has done the task already ask for any adjustment that he need in his time-table. At the end of the day, after 10:00 PM ask the user the user to provide the to do list and repeat the whole time-table building and assisting task again for the next day. IF YOU UNDERSTAND YOUR ROLE RELPY AS "YESS MASTER", after which I will proceed to give you the to-do list. Please write in English language.'}]


def gtp_responce(text):
    global messages

    messages.append({"role":"user","content": text})

    responce = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)
    system_message = responce["choices"][0]["message"]
    messages.append(system_message)
    #print(type(system_message['content']))
    #print(system_message['content'])
    #subprocess.call([ "say", system_message['content'] ])

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ":  " \
                                 + message['content']+ "\n\n"

    return [chat_transcript, system_message['content'] ]

# print("Enter 1 to start session: \n")
# choice = input()
# while choice == "1":
#     print("enter your prompt \n")
#     text = input()
#     chat_transcript = gtp_responce(text)
#     print(chat_transcript[0]+"\n")
#     print("system responce : "+ chat_transcript[1] +'\n')
#     print("Press 1 to continue :\n")
#     choice = input()

