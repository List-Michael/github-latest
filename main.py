import sys
import json

import requests


if __name__ == "__main__":
    username = sys.argv[1]

    response = requests.get(f"https://api.github.com/users/{username}/events")
    events = json.loads(response.content)
    print(events[0]['created_at'])