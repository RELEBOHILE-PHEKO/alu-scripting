#!/usr/bin/python3
"""
Contains the number_of_subscribers function.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers for the given subreddit, or 0 if an error occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'API-Advanced'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
