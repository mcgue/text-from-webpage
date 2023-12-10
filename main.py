# Obtain list of five words with more than 8 letters from random wikipedia page

import requests
from bs4 import BeautifulSoup

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.body.contents[0])
    text = soup.get_text()
    print(text)
