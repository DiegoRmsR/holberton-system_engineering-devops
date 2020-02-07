#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ first 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent': user_agent}
    params = {'limit': 10}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return(None)
    rdict = res.json()
    post_hot = rdict.get('data')['children']
    for post in post_hot:
        print(post.get('data')['title'])
