# COLLECTS URLS FROM PAGE SEARCH
# import libraries

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# environment set up
os.environ["LANG"] = "en_US.UTF-8"
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
yahoo_home_url = 'https://chiebukuro.yahoo.co.jp/'
driver.get(yahoo_home_url)

business_words_df = pd.read_csv('business_words.csv')
business_words_df = business_words_df[business_words_df['word'].notna()]
words = business_words_df['word'].tolist()

wait = WebDriverWait(driver, 10)
action = ActionChains(driver)


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True


# 30 search pages, 10 searches per page = 300 searches

links = []
ranks = []
seed_words = []

for k in range(len(words)):
    word = words[k]
    print(str(k) + ' out of ' + str(len(words)) + ': ' + word)
    driver.get(yahoo_home_url)
    time.sleep(5)
    search_text_bar = driver.find_element(By.XPATH, '//*[@id="Top"]/div/div[1]/div/nav/div[1]/div/div/div/input')
    action.move_to_element(search_text_bar).click().send_keys(word).perform()
    action.move_to_element(search_text_bar).click().send_keys(Keys.ENTER).perform()
    time.sleep(5)

    for i in range(1, 31):
        print('Processing page ' + str(i))
        page_search_beg = "//a[text()='"
        page_search_end = "']"
        page_search = page_search_beg + str(i) + page_search_end

        if i != 1:
            if check_exists_by_xpath(page_search):
                page_button = driver.find_element(By.XPATH, page_search)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(page_button)).click()
                time.sleep(5)
            else:
                break

        for j in range(1, 11):
            x_path_beg = '//*[@id="sr"]/ul/li['
            x_path_end = ']/h3/a'
            x_path_url = x_path_beg + str(j) + x_path_end
            if check_exists_by_xpath(x_path_url):
                link_url = driver.find_element(By.XPATH, x_path_url).get_attribute("href")
                rank = ((i - 1) * 10) + j
                links = links + [link_url]
                ranks = ranks + [rank]
                seed_words = seed_words + [word]
            else:
                break

url_df = pd.DataFrame(columns=['seed_word', 'rank', 'url'])
url_df = url_df.assign(seed_word=seed_words, rank=ranks, url=links)

word_id = []
for i in range(1, len(words)+1):
    word_id = word_id + [i]

word_df = pd.DataFrame(columns=['word', 'word_id'])
word_df = word_df.assign(word=words, word_id=word_id)
word_df.to_csv('word_df.csv', sep=',', encoding='utf-8')

url_df_word_id = []
for i in range(len(url_df)):
    word = url_df['seed_word'][i]
    for j in range(len(word_df)):
        test_word = word_df['word'][j]
        if word == test_word:
            test_id = word_df['word_id'][j]
            url_df_word_id = url_df_word_id + [test_id]

url_df['word_id'] = url_df_word_id
url_df.to_csv('url_df.csv', sep=',', encoding='utf-8')