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
    
    '''
    Construct the Reddit API URL for the specified subreddit
    '''
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    '''
    Send an HTTP GET request to the API with a custom user-agent header
    '''
    response = requests.get(url, headers={'User-agent': 'I am learning Apis'})

    if response.status_code == 200:
        '''
        If the response status code is 200 (OK), the request was successful
        '''
        '''
        Parse the response JSON to extract subreddit title and subscribers count
        '''
        content = response.json()
        result = {"title": content['data']['title'],
                  "subscribers": content['data']['subscribers']}
        print(result)
    elif response.status_code == 404:
        '''
        If the response status code is 404, the subreddit was not found
        '''
        return 0
    else:
        '''
        Handle other response status codes with an exception or specific value
        '''
        raise Exception(f"Request failed with status code: {response.status_code}")
