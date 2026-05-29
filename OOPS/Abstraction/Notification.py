from abc import ABC , abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Notification):

    def send(self):
        print("Sending Email")

class SMS(Notification):

    def send(self):
        print("Sending SMS")

n1 = Email()
n2 = SMS()

n1.send()
n2.send()