class Notification:
    """Класс отправки сообщения (родитель)"""
    list_notification = [] # Список объектов куда отправляем сообщение

    def __init__(self,title, message): #Инициализатор экземпляра отправки сообщения
        self.title = title # Атрибут
        self.message = message
        self.list_notification.append(self) #< - В список добавляем объект

    def info(self):
        pass

    def send(self):
        for i in self.list_notification:
            i.send

class EmailNotification(Notification):
    def __init__(self,title,message,mail):
        super().__init__(title,message)
        self.mail = mail

    def send(self):
        print(f" 📧 Email {self.mail} | {self.title}: {self.message} ")

class SMSNotification(Notification):
    def __init__(self,title,message,phone):
        super().__init__(title,message)
        self.phone = phone

    def send(self):
        print(f" 📱 {self.phone} | {self.title}: {self.message} ")

class  PushNotification(Notification):
    def __init__(self,title, message,devise_id):
        super().__init__(title,message)
        self.devise_id = devise_id

    def send(self):
        print(f" Push {self.devise_id} | {self.title}: {self.message}" )


email = EmailNotification("Заказ принят","Заказ №123 принят", "mail@mail.ru")

sms = SMSNotification("Код: 1234","Не кому не сообщайте код","+70000000000")

push = PushNotification("Акция","ВНИМАНИЕ СКИДКА 10%", "devise_dsre23fd")


for item in Notification.list_notification:
    item.send()
