from tkinter import *
from playsound import playsound
import datetime
import time

#-------FUCTION FOR ALARM CLOCK------
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg = "Current Time: " + str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            print("TAKE A BREAK")
            playsound("Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3")
            break


def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{minn.get()}:{sec.get()}"
    Alarm(alarm_set_time)



#--- UI INTERFACE CREARTION-----
window = Tk()
window.title("ALARM CLOCK")

#---- IMAGE INSTALLATION--------
canvas = Canvas(width=400,height=400)
image_used = PhotoImage(file="pngwing.com (2).png")
canvas.create_image(150,150, image=image_used)
canvas.grid(column=0,row=0)

hour = StringVar()
minn = StringVar()
sec = StringVar()

#---- HOUR -------
hour_label = Label(text="Hours", font=("Arial", 16))
hour_label.place(x=10,y=255)
#-----SPINBOX FOR HOUR -------
hour_spinnbox = Spinbox(from_=0, to=24, width=5,textvariable=hour)
hour_spinnbox.place(x=55,y=255)
#----MINUTES--------
minute_label = Label(text="Minutes", font=("Arial", 16))
minute_label.place(x=125,y=255)

minute_spinnbox = Spinbox(from_=0, to=60, width=5,textvariable=minn)
minute_spinnbox.place(x=190,y=255)
#----SECOND-------
second_label = Label(text="Seconds", font=("Arial", 16))
second_label.place(x=260,y=255)

second_spinnbox = Spinbox(from_=0, to=60, width=5,textvariable=sec)
second_spinnbox.place(x=325,y=255)
#----ALARM BUTTON-----
set_alarm_button = Button(text="SET ALARM",command=get_alarm_time)
set_alarm_button.place(x=125,y=300)

window.mainloop()