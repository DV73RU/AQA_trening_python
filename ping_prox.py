import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

#После скана живые прокси лягут в файл alive-proxies.txt

# --- читаем прокси ---
with open("proxy-list.txt", "r", encoding="utf-8") as f:
    proxies = [
        f"http://{line.strip()}"
        for line in f
        if line.strip()
    ]


lock = threading.Lock()
total = len(proxies)
done = 0


def check_proxy(proxy):
    global done

    url = "https://api.ipify.org"

    try:
        start = time.time()

        r = requests.get(
            url,
            proxies={"http": proxy, "https": proxy},
            timeout=5
        )

        latency = round((time.time() - start) * 1000, 2)

        # --- пишем live в файл ---
        with lock:
            with open("alive-proxies.txt", "a", encoding="utf-8") as f:
                f.write(proxy.replace("http://", "") + "\n")

        done += 1
        print(f"[{done}/{total}] OK   | {proxy} | {latency} ms")

    except Exception as e:
        done += 1
        print(f"[{done}/{total}] FAIL | {proxy}")


def run(workers=20):
    # очищаем файл перед стартом
    open("alive-proxies.txt", "w").close()

    print(f"Checking {total} proxies...\n")

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(check_proxy, p) for p in proxies]

        for _ in as_completed(futures):
            pass

    print("\nDONE")
    print("Alive saved to alive-proxies.txt")


run()