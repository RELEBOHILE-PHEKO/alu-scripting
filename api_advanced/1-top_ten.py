#!/usr/bin/python3
"""Top Ten Posts from Reddit"""

import requests

def top_ten(subreddit):
    """Fetches and prints titles of the first 10 hot posts from a subreddit."""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
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
