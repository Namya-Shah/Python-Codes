from socket import timeout
import time
from plyer import notification
if __name__ == '__main__':
    try:
        while True:
            notification.notify(
                title = "Take a class",
                message = "I have to take a python workshop",
                timeout = 10
            )
            time.sleep(15)
    except NotImplementedError:
        print("You have no use of using notification method.")