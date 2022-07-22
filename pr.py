time1 = input("Enter time: ")

hours, minutes = time1.split(":")

new_minutes = int(minutes)/60
print(new_minutes)
new_time = str(hours) + "." + str(new_minutes)
print(new_time)

if "7.00" <= new_time < "8.00":
    print("Breakfast Time")
elif "12.00" <= new_time < "13.00":
    print("Lunch Time")
elif "18.00" <= new_time < "19.00":
    print("Dinner Time")