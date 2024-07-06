#!/usr/bin/python3
"""Contains the number_of_subscribers function"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers if the request is successful, otherwise 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "API-Advanced"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return 0

    try:
        subs = response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0

    return subs
