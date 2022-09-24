# EXTRACT TEXT FROM HTML FILES
# import libraries

import pandas as pd
import os
from bs4 import BeautifulSoup


# environment set up
os.environ["LANG"] = "en_US.UTF-8"
url_df = pd.read_csv('url_df.csv')
url_df = url_df.drop(columns=['Unnamed: 0'])

texts = []
for i in range(len(url_df)):
    print('Processing ' + str(i) + ' out of ' + str(len(url_df)))
    file_path = 'html_files/' + str(url_df['word_id'][i]) + '_' + str(url_df['rank'][i]) + '.html'
    if os.path.isfile(file_path):
        html_file = open(file_path, "r")
        index = html_file.read()
        soup = BeautifulSoup(index, 'lxml')
        if soup.findAll('p', {'class': 'yjSlinkDirectlink ClapLv1TextBlock_Chie-TextBlock__Text__1jsQC ClapLv1TextBlock_Chie-TextBlock__Text--mediumRelative__3HSR8 ClapLv1TextBlock_Chie-TextBlock__Text--SpaceOut__3kF8R ClapLv1TextBlock_Chie-TextBlock__Text--preLine__2SRma'}):
            question = soup.find('p', {'class': 'yjSlinkDirectlink ClapLv1TextBlock_Chie-TextBlock__Text__1jsQC ClapLv1TextBlock_Chie-TextBlock__Text--mediumRelative__3HSR8 ClapLv1TextBlock_Chie-TextBlock__Text--SpaceOut__3kF8R ClapLv1TextBlock_Chie-TextBlock__Text--preLine__2SRma'}).text
            if soup.findAll('h2', {'class': 'ClapLv1TextBlock_Chie-TextBlock__Text__1jsQC ClapLv1TextBlock_Chie-TextBlock__Text--large__2SXOJ ClapLv1TextBlock_Chie-TextBlock__Text--bold__QVRZq'}):
                best_answer = soup.find('h2', {'class': 'yjSlinkDirectlink ClapLv1TextBlock_Chie-TextBlock__Text__1jsQC ClapLv1TextBlock_Chie-TextBlock__Text--mediumRelative__3HSR8 ClapLv1TextBlock_Chie-TextBlock__Text--SpaceOut__3kF8R ClapLv1TextBlock_Chie-TextBlock__Text--preLine__2SRma'}).text
                text = question + '<break>' + best_answer
                texts = texts + [text]
            else:
                text = question
                texts = texts + [text]
        else:
            texts = texts + ['NA']
    else:
        texts = texts + ['NA']

url_df['text'] = texts
url_df = url_df.drop(url_df[(url_df['text'] == 'NA')].index)
url_df.to_csv('url_df.csv', sep=',', encoding='utf-8')