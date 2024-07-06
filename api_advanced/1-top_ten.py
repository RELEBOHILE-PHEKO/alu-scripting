#!/usr/bin/python3
"""" Top Ten Limit"""
import requests


def top_ten(subreddit):
    """"top ten"""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_headers = {
        "User-Agent": "API-Advanced"
        }

  response = requests.get(URL, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch posts: Status Code {response.status_code}")
        return
    
    try:
        json_response = response.json()
        posts = json_response['data']['children']
        for post in posts:
            print(post['data']['title'])
    except KeyError as e:
        print(f"Failed to parse response: Missing key {e}")
