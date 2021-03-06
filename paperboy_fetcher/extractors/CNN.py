"""
As of Mid April 2020, the code below will extract the article text from CNN news articles.
It might catch bylines
Note: This extractor seems to work only on links that end in index.html. The other links form
a different format, probably because of video etc
"""
from bs4 import BeautifulSoup

def extract_article(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string
    body = soup.find(attrs={'itemprop': 'articleBody'})
    content = []
    # we have both divs a p nodes, TODO: Functionalize this if it gets any more
    content_nodes = body.find_all('p', attrs={'class': 'zn-body__paragraph speakable'})
    for node in content_nodes:
        for chunk in node.strings:
            content.append(chunk)
    content_nodes = body.find_all('div', attrs={'class': 'zn-body__paragraph'})
    for node in content_nodes:
        for chunk in node.strings:
            content.append(chunk)

    article = ' '.join(content)
    return {
        'title': title,
        'article': article
    }