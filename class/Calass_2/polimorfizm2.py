#TODO написать минимальные проверки передачи URL

class ChromeBrowser:

    def open_page(self, url):  # Метод принимает url
        # Проверка валидности строки
        if isinstance(url, str) and  url.strip() and url.startswith(("https://", "http://")):
            return f"{__class__.__name__} -> Открыт URL: {url}"

        else:
            raise ValueError(f"В {__class__.__name__} Передали не валидный URL: {url}")

class FirefoxBrowser:

    def open_page(self, url):
        if isinstance(url, str) and  url.strip() and url.startswith(("https://", "http://")):
            return f"{__class__.__name__} -> Открыт URL: {url}"

        else:
            raise ValueError(f"В {__class__.__name__} Передали не валидный URL: {url}")

url = "ttps://gogole.com"
chrome = ChromeBrowser()
firefox = FirefoxBrowser()

list_browser = [chrome, firefox]
for browser in list_browser:
    try:
        print(browser.open_page(url))
    except ValueError as err:
        print(err)

