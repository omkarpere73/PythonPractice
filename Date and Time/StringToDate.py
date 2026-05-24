from datetime import datetime

date = "24-05-2026"

d = datetime.strptime(date, "%d-%m-%Y")

print(d)