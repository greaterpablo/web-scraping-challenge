#Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
#NASA MARS NEWS
    url = 'https://redplanetscience.com/'

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')

    #Get title names and teaser on https://redplanetscience.com/
    general_scrape = soup.find('div',id='news')
    titles = general_scrape.find_all('div',class_="content_title")
    teaser = general_scrape.find_all('div',class_="article_teaser_body")
    list_news = []
    for x in range(len(titles)):
        dictio = {"title":titles[x].text,"teaser":teaser[x].text}
        list_news.append(dictio)
    browser.quit()
#JPL MARS SPACE IMAGES
    url = 'https://spaceimages-mars.com/'
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    #Get images from https://spaceimages-mars.com/
    general_scrape_images = soup.body.find('div',class_='thmbgroup')
    images = general_scrape_images.find_all('a')
    list_images = []
    for image in images:
        list_images.append(url+image['href'])
    browser.quit()
#Mars Facts
    url = 'https://galaxyfacts-mars.com/'
    facts = pd.read_html(url)[1]
    facts = facts.rename(columns={0:"Fact",1:"Information"})
    facts_html = facts.to_html()
    facts_html
#Mars Hemispheres
    url = 'https://marshemispheres.com/'
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)
    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')
    #Get images from https://spaceimages-mars.com/
    hemisphere_scrape_links = soup.body.find('div',class_='collapsible results')
    hemisphere_links = hemisphere_scrape_links.find_all('a',class_="itemLink product-item")
    hemisphere_image = []
    for link in hemisphere_links:
        img_dict = {}
        if link.h3 is None:
            link_path = link["href"]
            browser.visit(url+link_path)
            html = browser.html
            soup = bs(html, 'html.parser')
            title = soup.body.find('h2',class_="title").text
            hem_image = soup.body.find('img',class_='wide-image')['src']
            img_dict["title"] = title
            img_dict["img_url"] = url+hem_image
            hemisphere_image.append(img_dict)
    browser.quit()
    print(hemisphere_image)
    dictionary_read = {
    "News": list_news,
    "Images": list_images,
    "Facts": facts_html,
    "Hemisphere":hemisphere_image
    }   
    return dictionary_read