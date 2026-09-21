"""
Иерархия Page Object. Есть BasePage с методом open() -> bool.
Наследники: LoginPage, CatalogPage, AdminPage. AdminPage требует авторизованного администратора.
Спроектируй классы так, чтобы общий код мог делать page.open() для любой страницы без isinstance() и без передачи дополнительных аргументов именно в AdminPage.open().
Подумай, где правильнее хранить пользователя или состояние авторизации.
"""

from abc import ABC, abstractmethod


class BasePage(ABC):

    @abstractmethod
    def open(self) -> bool:
        pass


class LoginPage(BasePage):
    def open(self) -> bool:
        return True


class CatalogPege(BasePage):
    def open(self) -> bool:
        return True


class AdminPage(BasePage):

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def open(self) -> bool:
            return self.user_name == "admin" and self.password == "Passw0rd!"


lg_page = LoginPage()
ct_page = CatalogPege()
admin_page = AdminPage("admin", "Passw0rd!")
lg_page.open()
ct_page.open()
admin_page.open()
