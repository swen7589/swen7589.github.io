
'''
INSTRUCTIONS:
There are no pre-built functions and doctests for this lab.
This is to get you more experience writing entire python programs from scratch.
Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive
Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        Trump has obviously sent tweets after 2018,
        but this particular archive of tweets has not been updated recently.
Step 3: Unzip each of these files to get files that look like `condensed_*.json`.
Step 4: Modify this `lab_part1.py` file so that it:
    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.
    2. Prints the total number of tweets.
    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many different capitalizations, 
       and your program should count the word no matter how it is capitalized.  
       For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.
    4. Prints out a count of each of these words.
My program gives the following output:
    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
You'll know your program is correct if you get the same numbers.
========================================
EXTRA CREDIT:
You may earn 2 points of extra credit on this lab if you also:
    1. select at least 3 more interesting words/phrases to count in trump's tweets,
    2. calculate the percentage of tweets that contain each word, and
    3. display them nicely.
The display must have all words right justified and the percents printed with two 
significant figures (on both sides of the decimal) as shown in the example output below.
For example:
    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
HINT:
There are many ways to achieve this effect in python,
but I recommend using the .format string function.
Your python cheat sheet has instructions.
========================================
Submission
Upload your completed `lab_part1.py` file to sakai,
and copy and paste the output of running your program into sakai.
'''

import json

# step 4 part 1
with open('condensed_2009.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2010.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2011.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2012.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2013.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2015.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2016.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2017.json', encoding = "ascii") as f:
    text = f.read()

with open('condensed_2018.json', encoding = "ascii") as f:
    text = f.read()


files = ['condensed_2009.json', 'condensed_2010.json', 'condensed_2011.json', 'condensed_2012.json', 'condensed_2013.json', 'condensed_2014.json', 'condensed_2015.json', 'condensed_2016.json', 'condensed_2017.json', 'condensed_2018.json']
text = ' '
for file in files:
    with open(file, encoding = "ascii") as f:
        text = f.read()

# step 4 part 2 (not done)
tweets = json.loads(text)

print(len(tweets))

# step 4 parts 3 and 4 (also not done)

#to find 'trump'
num_trumps = 0

for tweet in tweets:
    
    if 'trump' in tweet['text'].lower():    
        num_trumps += 1

print('num_trumps=', num_trumps)

#to find 'obama'
num_obamas = 0

for tweet in tweets:
    
    if 'obama' in tweet['text'].lower():   
        num_obamas += 1

print('num_obamas=', num_obamas)

#to find 'russia'
num_russias = 0

for tweet in tweets:
    
    if 'russia' in tweet['text'].lower():    
        num_russias += 1

print('num_russias=', num_russias)

#to find 'mexico'
num_mexicos = 0

for tweet in tweets:
    
    if 'mexico' in tweet['text'].lower():   
        num_mexicos += 1

print('num_mexicos=', num_mexicos)

#to find 'fake news'
num_fakes = 0

for tweet in tweets:
    
    if 'fake news' in tweet['text'].lower():   
        num_fakes += 1

print('num_fakes=', num_fakes)

# find the answers in wednesday_secs because we didnt go 
# through all of this stuff in class ahaha (:
