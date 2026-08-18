class BasePage:
    """Класс родитель"""

    def __init__(self, url: str, title: str):
        self.url = url  # URL страницы
        self.title = title  # Заголовок страницы

    def is_opened(self):
        """
        Метод проверки страницы
        Проверка url
        Проверка заголовка (title)
        """
        return self.url.endswith("") and self.title == ""


class LoginPage(BasePage):
    """Класс проверки авторизации """

    # title = "Автодок. Вход и регистрация"
    # url = "https://login.autodoc.ru/Account/Login"

    def is_opened(self):
        return self.url.endswith(
            "/Login") and self.title == "Вход и регистрация"  # Не правильный title,  url правильный =   False


class CatalogPage(BasePage):
    """Класс открытие страницы каталога"""

    # url = "https://www.autodoc.ru/catalogs/"
    # title = "Купить запчасти для иномарок в интернет-магазине Автодок."

    def is_opened(self):
        return self.url.endswith(
            "/catalog") and self.title == "Купить запчасти для иномарок в интернет-магазине Автодок."  # Не правильный url , заголовок правильный False


class CartPage(BasePage):
    """Класс открытие страницы корзины"""

    # url = "https://www.autodoc.ru/cart"
    # title = "Корзина – Автодок"

    def is_opened(self):
        return self.url.endswith("/cart") and self.title == "Корзина – Автодок."  # Всё правильно True


def check_pages(list_pages):
    """
    Функция проверки страниц.
    Принимает список объектов страниц
    """

    list_messages = []  # Список сообщений от методов
    for page in list_pages:  # Пройдись по списку объектов
        class_name = page.__class__.__name__  # получаем имя каждого класса переданного в списке
        message = page.is_opened()  # Результат выполнения метода в каждом объекте запиши в переменную
        full_message = f"{class_name}: {message}"
        list_messages.append(full_message)  # Добавь в результат(сообщение в список)
    return list_messages  # Верни весь список


authorization = LoginPage("https://www.autodoc.ru/catalogs/",
                          "Купить запчасти для иномарок в интернет-магазине Автодок.")
catalog = CatalogPage("https://www.autodoc.ru/cart", "Купить запчасти для иномарок в интернет-магазине Автодок.")
cart = CartPage("https://www.autodoc.ru/cart", "Корзина – Автодок.")

list_object_pages = [authorization, catalog, cart]

for check in check_pages(list_object_pages):  # Пройдись по списку полученном функцией
    print(check)
