#!/usr/bin/python3
"""Reddit API word counting module."""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Count occurrences of words from word_list in hot posts of a subreddit"""

    if word_count is None:
        word_count = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'API-Advanced'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title_words = post['data']['title'].lower().split()
            for word in word_list:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + title_words.count(word)

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    except Exception:
        return