"""
3. Работа с браузерами

Создай абстрактный класс BaseBrowser с двумя абстрактными методами:

open_page(url)
close()

Создай классы:

ChromeBrowser;
FirefoxBrowser.

Каждый браузер должен по-своему реализовать оба метода.

Попробуй создать дочерний класс SafariBrowser, реализовав только open_page(), и проверь, позволит ли Python создать его объект.
"""

from abc import ABC, abstractmethod


class BaseBrowser(ABC):
    """Родительский абстрактный класс """


    @abstractmethod
    def open_page(self, url):
        """Метод открытия url в браузере"""
        return

    @abstractmethod
    def close(self):
        """Метод закрывает браузер"""
        return


class ChromeBrowser(BaseBrowser):
    """Класс отрытия url в Chrome"""

    def open_page(self, url):
        return f"Открыта {url} в браузере Chrome..."

    def close(self):
        return f"Закрыт браузер Chrome"


class FirefoxBrowser(BaseBrowser):

    def open_page(self, url):
        return f"Открыта {url} в браузере Firefox..."

    def close(self):
        return f"Закрыт браузер Firefox"

# Не создаст экземпляр так как нет абстрактного метода close
class SafariBrowser(BaseBrowser):
    def open_page(self, url):
        return f"Открыт {url} в браузер Safari"


try:
    chrome = ChromeBrowser()
    firefox = FirefoxBrowser()
    safari = SafariBrowser() # <- TypeError: Can't instantiate abstract class SafariBrowser without an implementation for abstract method 'close'
except TypeError as err:
    print(err)

print(chrome.open_page("ya.ru"))
print(chrome.close())
print(firefox.open_page("ya.ru"))
print(firefox.close())