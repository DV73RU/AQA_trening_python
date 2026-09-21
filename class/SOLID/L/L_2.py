"""
Неправильный тип результата. Есть BasePage с методом is_opened() -> bool.
Сделай LoginPage, который возвращает корректный bool, и CartPage, который сначала нарушает контракт, возвращая строку.
Затем исправь CartPage. Проверь мысленно, сможет ли функция check_page(page) одинаково работать с обоими классами.

"""

from abc import ABC, abstractmethod


class BasePage(ABC):
    """Класс страница"""
    @abstractmethod
    def is_opened(self) -> bool:
        """Метод проверки страницы"""
        pass


class LoginPage(BasePage):
    """Класс страница логина"""

    def is_opened(self) -> bool:
        """Метод проверки страницы логина"""
        return True


# class CartPage(BasePage):
#     """Класс страницы Корзина"""
#     def is_opened(self) -> bool:
#         return "Открыта страница Корзина" # <- Нарушение принципа LSP

class CartPage(BasePage):
    """Класс страницы Корзина"""

    def is_opened(self) -> bool:
        return False
