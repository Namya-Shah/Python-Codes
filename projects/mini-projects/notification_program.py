from socket import timeout
import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Take a class",
            message = "I have to take a python workshop",
            timeout = 10
            )
        time.sleep(15)