#!/usr/bin/python3
"""Top Ten Posts from Reddit"""
import requests


def top_ten(subreddit):
    """first 10 hot posts from a subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_headers = {
        "User-Agent": "API-Advanced"
    }

    try:
        response = requests.get(URL, headers=my_headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except requests.RequestException as e:
        print(f"Error fetching subreddit posts: {e}")
