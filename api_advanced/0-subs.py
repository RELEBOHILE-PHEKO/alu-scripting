#!/usr/bin/python3
"""Contains number_of_subscribers function"""


import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "API -Advanced"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
