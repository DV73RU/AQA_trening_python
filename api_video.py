import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env (где хранится OPENAI_API_KEY)
load_dotenv()


# Инициализируем клиент OpenAI
client = OpenAI()


def generate_video_example():
    print("🚀 Отправка запроса на генерацию видео...")

    # 1. Создаем задачу на генерацию видео
    video_job = client.videos.create(
        model="sora-2",  # Доступные модели: sora-2 или sora-2-pro
        prompt="A cute calico cat wearing sunglasses playing a miniature piano on a sunny beach",
        # Дополнительно можно передать размеры и длительность, например:
        # size="720x1280",
        # seconds=4
    )

    job_id = video_job.id
    print(f"✅ Задача успешно создана. ID задачи: {job_id}")
    print("⏳ Ожидание генерации (это может занять пару минут)...")

    # 2. Опрашиваем API, пока видео не будет готово (Polling)
    while True:
        # Получаем актуальный статус задачи
        status_check = client.videos.retrieve(job_id)
        status = status_check.status

        if status == "completed":
            # Видео готово, получаем ссылку на скачивание
            video_url = status_check.output.video_url
            print(f"\n🎉 Видео готово! Ссылка для скачивания:")
            print(video_url)
            break

        elif status == "failed":
            print(f"\n❌ Ошибка генерации: {status_check.error.message}")
            break

        else:
            # Если статус 'queued' (в очереди) или 'processing' (обрабатывается)
            print(".", end="", flush=True)
            time.sleep(15)  # Проверяем каждые 15 секунд


if __name__ == "__main__":
    generate_video_example()
