#!/usr/bin/python3
"""Contains top_ten function"""
import requests
import json

def fetch_subreddit_data(subreddit):
    """Fetch data from a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Your Unique User Agent Identifier"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.json()
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return None

def print_top_ten_titles(data):
    """Print the titles of the top 10 hottest posts"""
    if data is None:
        print("None")
        return
    results = data.get("data")
    if results:
        for child in results.get("children"):
            print(child.get("data").get("title"))

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit"""
    data = fetch_subreddit_data(subreddit)
    print_top_ten_titles(data)
