from plyer import notification
import time

if __name__ == "__main__":
    while True:
     notification.notify(
        title="take rest",
        message="This is the message of the notification.",
        app_icon=None,  # You can specify an icon path if you want
        timeout=5)  # Duration in seconds for which the notification will be visible
     time.sleep(7) #this is the time interval between notifications for 20 seconds

   #pythonw notification.py file will run in the background without opening a console window 