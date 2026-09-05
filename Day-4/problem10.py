time = input()

hour = int(time[:2])
minute = time[3:5]
second = time[6:8]
period = time[8:]

if period == "AM":
    if hour == 12:
        hour = 0
else:
    if hour != 12:
        hour += 12

print(f"{hour:02d}:{minute}:{second}")