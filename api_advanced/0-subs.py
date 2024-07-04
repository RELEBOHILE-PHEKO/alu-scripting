#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests

def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'linux:alu-scripting:v1.0.0 (by /u/Mpho_19)'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs