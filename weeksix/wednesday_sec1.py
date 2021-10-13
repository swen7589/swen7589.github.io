tweets = [
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]

tweets_str = '''[
    {   "source": "Twitter Web Client", 
        "id_str": "6312794445", 
        "text": "Trump International Tower in Chicago ranked 6th tallest building in world by Council on Tall Buildings & Urban Habitat http://bit.ly/sqvQq", 
        "created_at": "Thu Dec 03 19:39:09 +0000 2009", 
        "retweet_count": 33,
        "favorite_count": 6
    },
    {   "source": "Twitter Web Client", 
        "id_str": "6971079756",
        "text": "From DONALD Trump: Wishing everyone a wonderful holiday & a happy, healthy, prosperous New Year. Let's think like champions in 2010!", 
        "created_at": "Wed Dec 23 17:38:18 +0000 2009",
        "retweet_count": 28,
        "favorite_count": 12
        
    }
]
'''

# pprint stands for pretty print - prints things out in terminal nicely (not exactly like
# how its formatted above but it will be organized better than before)

import json
tweets = json.loads(tweets_str)

# JSON files are a special type of file that contain python code 
# that can be loaded with the json.load function

'''
with open('weeksix/condensed_2009.json', encoding = "ascii") as f:
    text = f.read()

with open('weeksix/condensed_2010.json', encoding = "ascii") as f:
    text = f.read()

with open('weeksix/condensed_2011.json', encoding = "ascii") as f:
    text = f.read()

files = ['weeksix/condensed_2009.json', 'weeksix/condensed_2010.json', 'weeksix/condensed_2011.json']
text = ' '
for file in files:
    with open(file, encoding = "ascii") as f:
        text = f.read()

import json
tweets = json.loads(text)
'''

# type[] shows the type of the name of the variable of what you put in between the brackets

'''
num_trumps = 0

for tweet in tweets:
    # if 'trump' in tweet['text']:
    # if 'Trump' in tweet['text']:
    # if 'trump' in tweet['text'].lower():
    f tweet['text'].find('trump') != -1:    # same as first if statement possibility
        num_trumps += 1

print('num_trumps=', num_trumps)

'''

# sec 1 part 2 #

# these are the term counts calculated in the lab
lab_dict = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

terms = lab_dict.keys()
counts = lab_dict.values()

# this code generates a plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts) # ax(x-axis, y-axis)
plt.show()

# pip3 install mathplotlib
