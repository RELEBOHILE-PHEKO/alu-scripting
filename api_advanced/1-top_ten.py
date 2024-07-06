#!/usr/bin/python3
""""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """"Print the titles of the 10 hottest posts on a given subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    my_headers = {
        "User-Agent": "API-Advanced"
        }

    response = requests.get(URL, headers=my_headers)
    # raw_response = response.json()['data']['children']

    if response.status_code != 200:
        print(None)
    else:
        json_response = response.json()
        posts = json_response['data']['children']
        [print(post.get('data').get('title')) for post in posts]
