Web Scraping - Mission to Mars

Scraping
Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of your scraping and analysis tasks. Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text.
- JPL Mars Space Images - Featured Image,
- Visited the url for JPL Featured Space Image here,
- Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.


Mars Facts
- Visited the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc,
- Used Pandas to convert the data to a HTML table string.


Mars Hemispheres
- Visited the USGS Astrogeology site obtained high resolution images for each of Mar's hemispheres.


MongoDB and Flask Application
Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

- scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data,
- Created a route called /scrape that will import scrape_mars.py,
- Stroed the return value in Mongo as a Python dictionary.,
- Created a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

![image](https://user-images.githubusercontent.com/63757160/109666738-17efb280-7b35-11eb-88fa-aaedbc732fa0.png)

![image](https://user-images.githubusercontent.com/63757160/109666793-250ca180-7b35-11eb-82dd-d6ccf331ee1e.png)

