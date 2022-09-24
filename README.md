# Building a Webscraper for Yahoo Answers

To solve any business problem or research question using data science, the first step is to collect your data.
Web scraping is the process of extracting and parsing data from websites in an automated fashion using a computer program.

In this application of webscraping, I built a web scraper that collects the best answer to questions from yahoo answers based on a list of search terms. A webscraper like this can be used for several different uses, such as expanding the corpus of an automatic speech recognition model to take into account domain specific words. 

After the webscraping, to increase useability, I separated the yahoo answer observations by sentence segment. I then cleaned these segments of urls and other noise. I then calculated the term frequency, document frequency and term frequency - inverse document frequency values to prep the corpus for analysis.

The yahoo answers website we will be scraping looks as such...



yahoo_webcrawl_4.ipynb : Text cleaning & tf-idf producing script
1. Cleans text (url_df_cleaned.csv)
2. Segments text into sentence sequences (sequence_webcrawl_cleaned_df.csv)
3. Creates nouns (名詞) list for tf-idf (nouns_list_all.txt)
4. Create term frequency for each noun over the same seed words (tf_by_seed_df.csv)
5. Create document frequency for each noun (名詞) (df_by_all.csv)
6. Create idf (df_by_all.csv)
7. Create tf_idf data frame by seed word for all nouns (名詞) (tf_idf_by_seed.csv)
