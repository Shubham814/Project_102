from plyer import notification
import time

while True:
    time.sleep(5)
    notification.notify(
        title = 'testing',
        message = 'message',
        app_icon = "water_glass.ico",
        timeout = 10,
    )