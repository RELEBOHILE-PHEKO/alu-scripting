#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    """"top ten"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_headers = {
        "User-Agent": "api-advanced/project"
        }

    response = requests.get(URL, headers=my_headers)
    # raw_response = response.json()['data']['children']

    if response.status_code != 200:
        print(None)
    else:
        json_response = response.json()
        posts = json_response['data']['children']
        [print(post.get('data').get('title')) for post in posts]
