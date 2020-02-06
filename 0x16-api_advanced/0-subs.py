#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Queries """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return 0
    rdict = res.json()
    result = rdict.get('data')['subscribers']
    if not result:
        return 0
    return result
