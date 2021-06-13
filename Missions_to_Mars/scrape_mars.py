#Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():

    mars_info = {}

#NASA MARS NEWS
    url = 'https://redplanetscience.com/'

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.quit()

    #extract data
    dates = soup.find_all('div', class_= 'list_date')
    titles = soup.find_all('div', class_= 'content_title')
    paragraphs = soup.find_all('div', class_= 'article_teaser_body')

    #save data
    news= []
    for i in range(0, len(dates)):
        news.append({
            'date': dates[i].text,
            'title': titles[i].text,
            'paragraph': paragraphs[i].text
        })
    
    mars_info['news'] = news

#JPL MARS SPACE IMAGES
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    browser.quit()

    featured_image_url = soup.find_all('img', class_= 'fancybox-image')
    featured_image_url = 'https://spaceimages-mars.com/'+featured_image_url[0]['src']

    #save data
    mars_info['feature_img'] = featured_image_url

#Mars Facts
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_urls = []

    for i in range(0, 4):
        links_found = browser.links.find_by_partial_text('Hemisphere Enhanced')
        links_found[i].click()
        html = browser.html
        soup = bs(html, 'html.parser')
    
        #retreive data
        title = soup.find('h2', class_= 'title').text
        img_url = soup.find('div', class_= 'downloads')
        img_url = img_url.find('a', target= '_blank')['href']
        img_url = 'https://marshemispheres.com/' + img_url
    
        hemisphere_image_urls.append({
            'Title': title,
            'Image URL': img_url
        })
    
        browser.links.find_by_partial_text('Back').click()

    browser.quit()

    #save data
    mars_info['hemisphere_imgs'] = hemisphere_image_urls

    ######################################################
    
    return mars_info