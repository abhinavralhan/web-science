import numpy as np
import string
from string import digits
import re
import matplotlib.pyplot as plt
import random
import seaborn as sns


f = open('Text_sample.txt', 'r',errors='ignore')
data = f.read()
textdata = data
punctuation_free_txt = textdata.translate(str.maketrans('','',string.punctuation))
lowercase_txt = punctuation_free_txt.lower()

text = re.findall('\w+',lowercase_txt)
new_dict = {}

for word in text:
    if word in new_dict:
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word] = 1

total_words = sum(new_dict.values())
probabilityDistribution = []

for key,value in sorted(new_dict.items()):
        probability = value / total_words
        probabilityDistribution.append(probability)

cumulativeProb = [probabilityDistribution[0]]

for x in range(len(probabilityDistribution)):
    if x+1 >= len(probabilityDistribution):
        break
    else:
        cdF = cumulativeProb[x] + probabilityDistribution[x+1]
        cumulativeProb.append(cdF)
x = []
y = cumulativeProb

for key,value in sorted(new_dict.items()):
    x.append(value)

counter = 0
GeneratedString = ''
while counter <= 5000:
    x = 0
    for key,value in sorted(new_dict.items()):
        randomInt = random.uniform(0,1)
        if randomInt > cumulativeProb[x]:
            counter +=1
            if counter > 5000:
                break
            GeneratedString = GeneratedString +' '+ key
            
        x+=1


new_dict = {}

punctuation_free_txt = GeneratedString.translate(str.maketrans('','',string.punctuation))
lowercase_txt = punctuation_free_txt.lower()

GeneratedStringtext = re.findall('\w+',lowercase_txt)

for word in GeneratedStringtext:
    if word in new_dict:
        new_dict[word] = new_dict[word] + 1
    else:
        new_dict[word] = 1

total_words = sum(new_dict.values())
probabilityDistributionGeneratedText = []

for key,value in sorted(new_dict.items()):
    probability = value / total_words
    probabilityDistributionGeneratedText.append(probability)

fig = plt.figure(figsize=(14,7))
plt.xlabel("Probability")
plt.ylabel("Density")
plt.title("Probability Distribution - Text Vs Generated Text")

plot1 = sns.kdeplot(probabilityDistributionGeneratedText)
plot2 = sns.kdeplot(probabilityDistribution)

plt.legend(['Generated Text', 'Input Text'], loc="upper right")

plt.savefig('ProbabilityDistribution.png')


f= open("generatedWords.txt","w+")
f.write(GeneratedString)
f.close()    

