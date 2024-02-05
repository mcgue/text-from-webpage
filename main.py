# Obtain list of five words with more than 8 letters from random wikipedia page

import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import random

def get_url():
    #set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )

    # verify getting valid response back and proceed if yes
    if (response.status_code) == 200:

        # Return url
        return response

    # try later if not working
    else:
        return 'Try again later'


# Run main
if __name__ == '__main__':
    #scraper
    response = get_url()

    # Get page and text
    soup = BeautifulSoup(response.text, 'html.parser')

    text = soup.body.get_text()

    # Turn page text into list
    text_list = text.split()

    text_list_8 = [i for i in text_list if len(i) > 7]

    # Get 5 random numbers between
    nums_random = []
    i=0
    while i < 5:
        j = random.randint(0,len(text_list_8))
        if j not in nums_random:
            nums_random.append(j)
            i+=1

    print(nums_random)

    print(text_list_8)
    # print(len(text_list))
