class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @classmethod
    def from_string(cls,data):
        """Метод класса, из строки во время"""
        # cls.data = data.split(":")
        hours, minutes, seconds = data.split(":")
        return cls(int(hours),int(minutes),int(seconds))


    @classmethod
    def from_second(cls,data):
        """Метод класса вернет время из секунд"""
        hours = data//3600
        minutes = (data % 3600) // 60
        seconds = data % 60
        return cls(hours,minutes,seconds)


    def info(self):
        """Метод экземпляра класса вернёт время"""
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")

t1 = Time(12,45,60)
t1.info()
t2 = Time.from_string("10:12:13")
t2.info()

t3 = Time.from_second(4245)
t3.info()