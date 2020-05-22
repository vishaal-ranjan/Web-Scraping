# Our aim through this piece of code is to go through all the quotes in the website
# and go through all the tags and then count the number of occurences of each tag
# following which we will arrange all the quotes in the decreasing order of their
# frequency of occurence

# Import all the necessary libraries
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# This is an object of a default dictionary
tags = defaultdict(int)

# This is the base URL
base = 'http://quotes.toscrape.com/'

# This is the list that will contain the addresses of the 10 pages that we'll visit for scraping
frontier = []
for i in range(10):
    frontier.append('page/{}'.format(i+1))

# We will loop through the frontier list so as to visit every page
for page in frontier:
    # We store the response from the requested web page
    response = requests.get(base + page)
    soup = BeautifulSoup(response.content, 'html.parser')

    # We want to find all the tags that have the 'a' symbol and iterate over all of those links
    for link in soup.find_all('a', {'class': 'tag'}):
        tags[link.text] += 1

print('Tags sorted in descending order of their frequency of occurences: \n')
for k, v in sorted(tags.items(), key = lambda item: item[1], reverse = True):
    print(k, ':', v)