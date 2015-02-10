import csv
from bs4 import BeautifulSoup
import requests

#Bib to URL List
museURLs = 'C:\\Users\\fenichele\\Desktop\\museURLs.csv'

def checkURL(url):
    """to check the URL of a muse journal"""

    museURL = url

    result = []

    response = requests.get(url, verify=True)

    s = response.status_code

    return s

def readURLs():
    """should load up the list of URLs for the BIBs"""

    bibURL = []
    with open(museURLs, 'r', encoding = 'utf-8') as csvfile:
        u = csv.reader(csvfile)
        for row in u:
            bibURL.append(row)

    return bibURL
            

def museCheck():
    bibURL = readURLs()

    for x in bibURL:
        bib = x[0]
        url = x[1]

        urlcode = checkURL(url)

        if urlcode == 200:
            pass
        else:
            print (bib,',',url)
            

    
    
    
