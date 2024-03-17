import os
import win32com.client as wincom


if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Muhammad Umer")
    while True:
        speak = wincom.Dispatch("SAPI.SpVoice")
        x = input("Enter what you want me to speak: ")
        if x == "0":
            speak.Speak("bye bye friend")
            break
        speak.Speak(x)

    #print("Welcome to RoboSpeaker 1.1. Created by Muhammad Umer")
    #x = input("Enter what you want me to speak: ")
    #command = f"say{x}"
    #os.system(command)
