class OpenFileContext:
    text = "Текст для вставки в файл"
    def __enter__(self):
        print(f"Открываем файл")
        open("txt.txt","w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Закрываем файл")
        if exc_type:
            print(f"Произошла ошибка {exc_type}")
        return False

with OpenFileContext():
    print(f"Работаем внутри")