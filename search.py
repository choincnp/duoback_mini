from bs4 import BeautifulSoup
import requests
import re

# CONSTANT 
REQ = {
    'KEY': 'User-Agent',
    'VALUE': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
}


#Modules
def getHTMLData(query):
    data = requests.get(f'https://www.youtube.com/results?search_query={query}', headers={REQ['KEY']: REQ['VALUE']})
    soup = BeautifulSoup(data.text, PARSER['TYPE'])
    return soup