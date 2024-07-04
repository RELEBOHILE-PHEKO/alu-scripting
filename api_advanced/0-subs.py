#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'linux:alu-scripting:v1.0.0 (by /u/Mpho_19)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0