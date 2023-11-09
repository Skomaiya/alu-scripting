#!/usr/bin/python3
"""
function that queries the 'Reddit API' and returns the number of subscribers
"""
import requests

<<<<<<< HEAD

def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyBot/1.0"}  # avoid Too Many Requests error
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()["data"]
        return data["subscribers"]
    else:
        return 0
=======
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
>>>>>>> 19411f52229f930d21c0a27c852c60af9034e004
