import time

#Returns current time in seconds since Jan 1, 1970 (Unix Epoch).
print(time.time())

#Converts timestamp into readable format.
print(time.ctime())

#Returns local time as a structured object.
t = time.localtime()
print(t)

#Pauses program execution.
print("Start")
time.sleep(3)
print("End after 3 seconds")

#Formats date/time into custom string.
print(time.strftime("%d-%m-%y"))


print(time.strftime("%A %d %B %Y"))