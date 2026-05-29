class mail:
    def send(self):
        print("Sending Mail")

class wp:
    def send(self):
        print("Sending Whatsapp Message")

class sms:
    def send(self):
        print("Sending SMS")

notifications = [mail() , wp() , sms()]

for n in notifications:
    n.send()