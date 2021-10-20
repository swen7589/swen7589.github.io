
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
with open('condensed_2009.json', 'r') as f1:
    text1 = f1.read()

with open('condensed_2010.json', 'r') as f2:
    text2 = f2.read()

with open('condensed_2011.json', 'r') as f3:
    text3 = f3.read()

with open('condensed_2012.json', 'r') as f4:
    text4 = f4.read()

with open('condensed_2013.json', 'r') as f5:
    text5 = f5.read()


with open('condensed_2014.json', 'r') as f6:
    text6 = f6.read()

with open('condensed_2015.json', 'r') as f7:
    text7 = f7.read()

with open('condensed_2016.json', 'r') as f8:
    text8 = f8.read()

with open('condensed_2017.json', 'r') as f9:
    text9 = f9.read()

with open('condensed_2018.json', 'r') as f10:
    text10 = f10.read()


files = ['condensed_2009.json', 'condensed_2010.json', 'condensed_2011.json', 'condensed_2012.json', 'condensed_2013.json', 'condensed_2014.json', 'condensed_2015.json', 'condensed_2016.json', 'condensed_2017.json', 'condensed_2018.json']
text = ' '
for file in files:
    with open(file) as f:
        text = f.read()

# step 4 part 2 
tweets1 = json.loads(text1)
tweets2 = json.loads(text2)
tweets3 = json.loads(text3)
tweets4 = json.loads(text4)
tweets5 = json.loads(text5)
tweets6 = json.loads(text6)
tweets7 = json.loads(text7)
tweets8 = json.loads(text8)
tweets9 = json.loads(text9)
tweets10 = json.loads(text10)

all_tweets = tweets1 + tweets2 + tweets3 + tweets4 + tweets5 + tweets6 + tweets7 + tweets8 + tweets9 + tweets10

print('total number of tweets:', len(all_tweets))

# step 4 parts 3 and 4 

term_counter = {}

terms = ['trump', 'obama', 'mexico', 'russia', 'fake news', 'china', 'sad', 'wall', 'border']

for term in terms:
    term_counter[term] = 0

for tweet in all_tweets:
    
    for term in terms:
        if term in tweet['text'].lower():
            term_counter[term] += 1

print(term_counter)

# extra credit

trump_percent = (term_counter['trump']/len(all_tweets)) * 100
print(f"trump : {trump_percent:.2f}%")

obama_percent = (term_counter['obama']/len(all_tweets)) * 100
print(f"obama : {obama_percent:.2f}%")
 
russia_percent = (term_counter['russia']/len(all_tweets)) * 100
print(f"russia : {russia_percent:.2f}%")
 
mexico_percent = (term_counter['mexico']/len(all_tweets)) * 100
print(f"mexico : {mexico_percent:.2f}%")
 
china_percent = (term_counter['china']/len(all_tweets)) * 100
print(f"china : {china_percent:.2f}%")
 
sad_percent = (term_counter['sad']/len(all_tweets)) * 100
print(f"sad : {sad_percent:.2f}%")
 
wall_percent = (term_counter['wall']/len(all_tweets)) * 100
print(f"wall : {wall_percent:.2f}%")

border_percent = (term_counter['border']/len(all_tweets)) * 100
print(f"border : {border_percent:.2f}%")
