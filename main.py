# check if tasks.json exists, if not create it
import json
import os

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as f:
        json.dump([], f)
        f.close()
