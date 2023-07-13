from tkinter import *
import tkinter as tk
from threading import Thread
import time as t
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()

# log keeper
def write_log(sent_by,message):
    thread = Thread(target=threading_function,args=(sent_by,message,))
    thread.start()

def threading_function(sent_by,message):
    text_file = open("Log_Folder/command_log.txt","a")
    text = str("\n"+ t.ctime(t.time())  + "\n " + sent_by + " : " + message + "\n")
    text_file.write(text)
    text_file.close()


# python text to speech
engine = pyttsx3.init()
def speak_offline(message):    
    engine.say(message)
    engine.runAndWait()
    engine.stop()

# speech recognition module
def listen():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        try:
            message = r.recognize_google(audio_text)
            print("Text: "+message)
        except:
            message = "unabe to recognize"
            print(message)
        return message


# user interface
root = Tk()
root.geometry("500x750")
root.title("Threading in python !!!")
root['bg'] = "white"

time=t.ctime(t.time())
time_label = Label(text = time,background="white",font=("arial",10),padx=20,pady=2)
time_label.pack(anchor=NE)
face = PhotoImage(file="Images/face-removebg-preview.png")
face= face.subsample(2,2)
face_ai = Button(root,text="face of ai",image=face,borderwidth=0,background="white")
face_ai.pack()
output_text = ">"

speak_list=[]
listening_list=[]


def search_go():
    output_text = str(input_command.get())
    input_command.delete(0,tk.END)
    write_log("user",output_text)
    result="ai module need to created"

    display_output(result)


def speak_search():
    output_text = listen()
    input_command.delete(0,tk.END)
    input_command.insert(tk.END,output_text)
    # ai responce
    result="ai module need to created"
    
    display_output(result)

def background_listening():
    while True:
        try:
            spy_read = listen()
            write_log("user : ",spy_read)
        except Exception as error:
            print("error",error)
        

def display_time():
    while True:
        try:
            t.sleep(1)
            time = t.ctime(t.time())
            time_label.config(text=time)
        except:
            print("exception : program stoped")

def display_output(message):
    write_log("santa :",message)
    output_label.config(text=message)
    speak_offline(message)

color_list = ["#E5E4E2","#DCDCDC","#DADBDD","#D3D3D3","#CECECE","#D1D0CE","#C2DFFF","#C6DEFF","#E3E4FA","#DBE9FA","#E6E6FA","#EBF4FA","#F0F8FF","#F8F8FF","#F0FFFF","#E0FFFF","#CCFFFF"]
def change_color():
    while True:
        for colors in color_list:
            # print("color change")
            t.sleep(1)
            root.config(background=colors)
            time_label.config(background=colors)
            face_ai.config(background=colors)
            # input_window.config(background=colors)
            # command.config(background=colors)
        

thread = Thread(target=display_time,daemon=True)
thread.start()

background_thread = Thread(target=background_listening,daemon=True)
background_thread.start()

color_thread = Thread(target=change_color,daemon=True)
color_thread.start()

input_window = tk.Canvas(background="white",border=0)


command = Label(input_window,text="Command : ",background="white",padx=20,pady=20)
command.grid(row=1,column=1)

input_command = tk.Entry(input_window,background="#d7e4fa",border=2,width=20,font=("Arial",16))
input_command.grid(row=1,column=2,pady=20)

mic_img = PhotoImage(file="Images\mic_ori-removebg-preview.png")
mic_img = mic_img.subsample(21,21)
mic_input = Button(input_window,border=1,text="speak",command=speak_search,image=mic_img,background="white")
mic_input.grid(row=1,column=3,padx=5)

search = Button(input_window,text="GO",background="white",border=2,command=search_go)
search.grid(row=1,column=4,padx=5)

input_window.pack(padx=30,pady=20)

output_label = Label(text=output_text,anchor=NW,font=("Arial"),background="#EBFEFF",border=1,height=20,width=40)
output_label.pack()

root.mainloop()





