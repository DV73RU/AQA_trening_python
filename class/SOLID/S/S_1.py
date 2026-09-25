from abc import ABC, abstractmethod
class NotificationService:
    def __init__(self,sender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)