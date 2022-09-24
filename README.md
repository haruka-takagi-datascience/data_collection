# Building a Webscraper for Yahoo Answers

To solve any business problem or research question using data science, the first step is to collect your data.
Web scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program.

In this application of webscraping, I built a web scraper that collects the best answer to questions from yahoo answers based on a list of search terms. A webscraper like this can be used for several different uses, such as expanding the corpus of an automatic speech recognition model to take into account domain specific words. 

After the webscraping, to increase useability, I separated the yahoo answer observations by sentence segment. I then cleaned these segments of urls and other noise. I then calculated the term frequency, document frequency and term frequency - inverse document frequency values to prep the corpus for analysis. This webscraping script uses selenium, pandas, BeautifulSoup & MeCab (Japanese Morpholoical Analyzer).

The yahoo answers website we will be scraping looks as such. Looping through the search terms, we will search the most relavent answers to each search term .
<img src="images/img_1.png">

For each search term we will be collecting the url links for 10 pages worth of search results.
<img src="images/img_2.png">

Then we will be scraping each url for the best answer at the top of the page. 
<img src="images/img_3.png">

There are 4 scripts in this webscraping process.
1. yahoo_webcrawl_1.py: collects urls from yahoo answer page search. With a maximum of 300 urls per search term.

This script outputs a dataframe of seed_word, rank, url and word_id.
<img src="images/img_4.png">



3. yahoo_webcrawl_2.py: Scrapes html files for saving from url list from yahoo_webcrawl_1.py
4. yahoo_webcrawl_3.py: From each html file, extracts 




yahoo_webcrawl_1.py : collect urls from yahoo answer page search
yahoo_webcrawl_2.py : from url list save the html files
yahoo_webcrawl_3.py : extract question and best answer from html files
yahoo_webcrawl_4.ipynb : Text cleaning & tf-idf producing script
1. Cleans text (url_df_cleaned.csv)
2. Segments text into sentence sequences (sequence_webcrawl_cleaned_df.csv)
3. Creates nouns (名詞) list for tf-idf (nouns_list_all.txt)
4. Create term frequency for each noun over the same seed words (tf_by_seed_df.csv)
5. Create document frequency for each noun (名詞) (df_by_all.csv)
6. Create idf (df_by_all.csv)
7. Create tf_idf data frame by seed word for all nouns (名詞) (tf_idf_by_seed.csv)
