# FROM URL LIST WRITES HTML FILES
# import libraries

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

# environment set up
os.environ["LANG"] = "en_US.UTF-8"
url_df = pd.read_csv('url_df.csv')
url_df = url_df.drop(columns=['Unnamed: 0'])

business_words_df = pd.read_csv('business_words.csv')
business_words_df = business_words_df[business_words_df['word'].notna()]
words = business_words_df['word'].tolist()

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

for i in range(len(url_df)):
    print(str(i) + ' out of ' + str(len(url_df)))
    url = url_df['url'][i]
    driver.get(url)
    html_source = driver.page_source
    time.sleep(5)
    html_filename = 'html_files/' + str(url_df['word_id'][i]) + '_' + str(url_df['rank'][i]) + '.html'
    file_object = open(html_filename, "w")
    file_object.write(html_source)
    file_object.close()

s3_links = []
for i in range(len(url_df)):
    s3_link = 's3://tmp.ap-northeast-1.206286158172/takagi/webcrawl_html_files/' + str(url_df['word_id'][i]) + '_' + str(url_df['rank'][i]) + '.html'
    s3_links = s3_links + [s3_link]

url_df['html_s3_url'] = s3_links
url_df.to_csv('url_df.csv', sep=',', encoding='utf-8')










