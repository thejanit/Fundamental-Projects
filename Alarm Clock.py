from datetime import datetime

user_alarm_time = input("Enter the time of alarm:HH:MM:SS\n")
alarm_hr = user_alarm_time[0:2]
alarm_min = user_alarm_time[3:5]
alarm_sec = user_alarm_time[6:8]

while True:
    now_time = datetime.now()
    current_hr = now_time.strftime("%H")
    current_min = now_time.strftime("%M")
    current_sec = now_time.strftime("%S")

    if alarm_hr == current_hr:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print("!!! Wake Up !!!")
                break