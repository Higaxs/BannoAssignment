
# coding: utf-8

# In[46]:

import collections
import requests
from bs4 import BeautifulSoup
response = requests.get("https://banno.com/")
content = response.content
c = collections.Counter()
c2 = collections.Counter()
alphanumeric = ""
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
for char in str(content):
    if char.lower() in alphabet:
        alphanumeric += char
c.update(alphanumeric)
c2.update(alphanumeric.lower())
print("Top 3 most common alphanumeric characters (Cases considered) and their counts:")
for letter, count in c.most_common(3):
    print("{0}: {1}".format(letter, count))
print("Top 3 most common alphanumeric characters (Cases ignored) and their counts:")
for letter, count in c2.most_common(3):
    print("{0}: {1}".format(letter, count))
print("Number of .png images:")
print(len(str(content).split(".png")) - 1)
twitterHandle = str(content).split("\">Twitter")[0].split("/")[-1]
print("Twitter Handle:")
print("@" + twitterHandle)
print("Number of times \"financial institution\" occurs in the text on the page:")
count = len(str(content).split("<body>")[1].split("</body>")[0].split("financial institution")) - 1
print(count)
print("Number of times \"financial institution\" occurs in the text of the html:")
count2 = len(str(content).split("financial institution")) - 1
print(count2)
response2 = requests.get("https://banno.com/features/")
content2 = response2.content
productCount = len(str(content2).split("flex-item feature-group-label")) - 1
print("The number of products offered on \"https://banno.com/features/\":")
print(productCount)


# In[ ]:



