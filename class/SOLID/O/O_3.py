"""
3. Проверка страниц сайта — простая

Создай классы страниц:

LoginPage;
CatalogPage;
CartPage.

Каждая страница хранит текущие url и title и самостоятельно определяет, открыта ли нужная страница.

Создай функцию check_page(page), которая возвращает результат проверки любого объекта страницы.

Добавление новой страницы не должно требовать изменения функции.
"""

from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, url: str, title: str):
        self.url = url
        self.title = title

    @abstractmethod
    def check_page(self) -> bool:  # <- Метод проверки страницы
        pass


class LoginPage(BasePage):
    def check_page(self) -> bool:
        return self.url.endswith('login.ru') and self.title == "Вход"


class CatalogPage(BasePage):
    def check_page(self) -> bool:
        return self.url.endswith('catalog.ru') and self.title == "Каталог"


class CartPage(BasePage):
    def check_page(self) -> bool:
        return self.url.endswith('cart.ru') and self.title == "Корзина"


def check_page(page: BasePage) -> str:
    result = page.check_page()
    return result
    # status = "Пройдена" if result else "Ошибка"  # Если метод вернул False
    #
    # return (
    #     f"--- Проверка класса {page.__class__.__name__} ---\n"
    #     f"URL: {page.url}\n"
    #     f"Title: {page.title}\n"
    #     f"Результат проверки: {status} ({result})\n"
    # )


login_page = LoginPage('login.ru', "Авторизация")
catalog_page = CatalogPage('catalog.ru', "Каталог")
cart_page = CartPage("cart.ru", "Корзина")

print(check_page(login_page))
print(check_page(catalog_page))
print(check_page(cart_page))
