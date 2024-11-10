import time

seconds = int(input("Ent: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"{mins:02}:{secs:02}", end="\r")
    time.sleep(1)
    seconds -= 1

print("00:00")
print("Time's up!")
