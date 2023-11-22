# Obtain list of five words with more than 8 letters from random wikipedia page

import requests

def get_url():
    #set up scraper for page
    response = requests.get(
        url="https://en.wikipedia.org/wiki/Special:Random",
    )

    # verify getting valid response back and proceed if yes
    if (response.status_code) == 200:

        # Return url
        return response.url

    # try later if not working
    else:
        return 'Try again later'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_url())
