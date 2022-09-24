# Building a Webscraper for Yahoo Answers

To solve any business problem or research question using data science, the first step is to collect your data.
Web scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program.

In this application of webscraping, I built a web scraper that collects the best answer to questions from yahoo answers based on a list of search terms. A webscraper like this can be used for several different uses, such as expanding the corpus of an automatic speech recognition model to take into account domain specific words. 

After the webscraping, to increase useability, I separated the yahoo answer observations by sentence segment. I then cleaned these segments of urls and other noise. I then calculated the term frequency, document frequency and term frequency - inverse document frequency values to prep the corpus for analysis.

The yahoo answers website we will be scraping looks as such. Looping through the search terms, we will search the most relavent answers to each search term .
<img src="images/img_1.png">

For each search term we will be collecting the url links for 10 pages worth of search results.
<img src="images/img_2.png">

Then we will be scraping each url for the best answer at the top of the page. 
<img src="images/img_3.png">

