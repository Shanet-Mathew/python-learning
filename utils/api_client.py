# utils/api_client.py

import requests


def get_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("API request failed")

    return response.json()