#!/usr/bin/python3
"""
    python script that returns subreddit subscribers
"""
import json
import requests


"""
    Define HTTP headers for the API requests
"""
def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'  # Fixed URL
    response = requests.get(url, headers={'User-agent': 'I am learning Apis'})

    if response.status_code == 200:
        content = response.json()
        result = {"title": content['data']['title'],
                  "subscribers": content['data']['subscribers']}
        return result
    elif response.status_code == 404:
        return 0
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
