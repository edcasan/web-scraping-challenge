from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    
    # NASA MARS NEWS

    # URL MARS NASA
    url='https://mars.nasa.gov/'
    response = requests.get(url)

    # bs object
    soup = bs(response.text, "html.parser")
    item_list_ul = soup.find_all('div', class_='list_text')[0]
    title=item_list_ul.find('h3',class_ = 'title').text
    browser = init_browser()
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' 
    browser.visit(url)
    html = browser.html

    # bs object
    soup = bs(html, 'html.parser')

    # full image
    full_image_button = browser.links.find_by_partial_text("FULL IMAGE")
    full_image_button.click()
    more_info_button = browser.links.find_by_partial_text("more info")
    more_info_button.click()
    new_page = bs(browser.html,'html.parser')
    featured_img = f"https://www.jpl.nasa.gov{new_page.find('img',class_ = 'main_image')['src']}"
    browser.quit()

    # MARS FACTS

    # URL to be scraped
    url= 'https://space-facts.com/mars/'

    #read table
    table = pd.read_html(url)
    fdf = table[0]
    fdf.columns=["Properties", "Values"]
    mars_fac = fdf.to_html(index=False, header=False)
    
    
    # MARS HEMISPHERES

    browser = init_browser()

    #page to scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    hemisphere_img = []

    #list of the Hemispheres
    for x in range(0,4):
        hemisphere = {}
        
        browser.find_by_css("a.product-item h3")[x].click()
        sample = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample["href"]
        hemisphere["title"] = browser.find_by_css("h2.title").text
        hemisphere_img.append(hemisphere)
        browser.back()

    browser.quit()

    # Store data
    mars_data = {
        "news_title": title,
        "featured_image": featured_img,
        "mars_facts": mars_fac,
        "hemispheres": hemisphere_img
    }

    return mars_data
