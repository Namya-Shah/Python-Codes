command = ""
started = False

while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car Started...")
    elif command.lower() == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car Stopped.")
    elif command.lower() == "help":
        print("Enter start to start the car")
        print("Enter stop to stop the car")
        print("Enter quit to quit the program")
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand that.")
        