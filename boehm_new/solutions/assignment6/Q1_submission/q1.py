#!/usr/bin/env python
# coding: utf-8

import re
import nltk
import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.stats import zipf
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Fetching all data

all_data = ''
for files in ['Text_0123/Text_0.txt', 'Text_0123/Text_1.txt', 'Text_0123/Text_2.txt', 'Text_0123/Text_3.txt']:
    f = open(files, 'r')
    data = f.read()
    all_data += data
    
# Creates sentence tokens and fetches the cleaned data

sentence_tokens = sent_tokenize(all_data)
for idx, sentence in enumerate(sentence_tokens):
    sentence_tokens[idx] = sentence_tokens[idx].replace('\n', ' ')
    
while True:
    sentence_tokens = [sentence for sentence in sentence_tokens if sentence != '']
    for idx, sentence in enumerate(sentence_tokens):
        if "Eq."in sentence or "eg." in sentence or "etc." in sentence:
            sentence_tokens[idx] = ' '.join(sentence_tokens[idx:idx+2])
            try:
                sentence_tokens[idx+1] = ''
            except:
                pass
    if '' not in sentence_tokens:
        break
all_data = ' '.join(sentence_tokens)

# Creates word tokens from cleaned sentences and words

word_tokens = word_tokenize(all_data)

cleaned_word_tokens = []

for word in word_tokens:
    if re.sub('[^A-Za-z]+', '', word) != '':
        cleaned_word_tokens.append(word)

cleaned_words = [word.lower() for word in cleaned_word_tokens]

# Plotting Data
data = pd.DataFrame(cleaned_words, columns=['word_tokens'])
data = data.word_tokens.value_counts().reset_index().rename(columns={'word_tokens': 'counts', 'index': 'word_tokens'})
data = data.reset_index().rename(columns={'index': 'rank'})
data['rank'] = data['rank'] + 1

plot_data_top50_words = data.head(50)
plot_data_top20_words = data.head(50)

total = plot_data_top50_words[:50].counts.sum()

plt.tight_layout()
sns.barplot(data=plot_data_top50_words, x='word_tokens', y='counts')

rcParams['figure.figsize'] = 16, 8
plt.xticks(rotation=90)
plt.savefig('plot_data_top50_words.png')
plt.show()

alpha = 2 # zipf distribution parameter
total = plot_data_top50_words[:50].counts.sum()

plt.plot(range(50), [zipf.pmf(p, alpha) * total for p in range(1, 51)], color='crimson', lw=3)
plt.tight_layout()
sns.barplot(data=plot_data_top50_words, x='word_tokens', y='counts')

rcParams['figure.figsize'] = 16, 8
plt.xticks(rotation=90)
plt.savefig('plot_data_top50_words_zipf.png')
plt.show()