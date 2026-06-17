import json
import time
from tqdm import tqdm

with open("large_data.json") as f:
    data = json.load(f)

for task in tqdm(data["tasks"]):
    time.sleep(task["duration"])


