import praw
import pprint
import random 

# FIXME:
# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
# 
# WARNING:
# If you include any credential information in your final submission,
# you will receive NEGATIVE POINTS on your lab!!!
reddit = praw.Reddit('idk_bot')

# connect to the "Main Discussion Thread" reddit submission
url='https://old.reddit.com/r/BotTown/comments/qqmr8l/main_discussion_thread/'
submission = reddit.submission(url=url)

# FIXME:
# Click the "view more comments" buttons in the reddit submission in order to download all comments.
#
# HINT:
# This step takes a long time.
# It takes the PRAW library about 1 second to "click" a link,
# and so it takes about 1 minute total to click all of them.
# I recommend saving this step for last since it will slow down your ability to run the steps below considerably.
# Get those working, then come back here and get this working.
submission.comments.replace_more(limit=None)

# FIXME:
# Loop through all the top level comments to calculate:
# 1. The total number of non-deleted top level comments,
# 2. The total number of deleted top level comments,
# 3. The total number of comments sent by each user.
#    You should use a dictionary where the keys are the username and the values are the total number of comments.

# 1 (non-deleted top level comments)
for top_level_comment in submission.comments:
    try:
        print(top_level_comment.body)
    except AttributeError:
        pass

print('total top-level comms=', len(submission.comments.list()))

# 2 and 3 (deleted top level comments and users)

not_deleted_comms = 0
deleted_comms = 0 
users = {}

for comment in submission.comments:
    if comment.author == None:
        deleted_comms += 1
    elif comment.author != None and comment.author not in users:
        users[comment.author] = 1
    elif comment.author != None and comment.author in users:
        users[comment.author] += 1
for comment in submission.comments:
    if comment.author != None:
        not_deleted_comms += 1

print('not deleted comments:', not_deleted_comms)
print('deleted comments:', deleted_comms)
print(users)

# FIXME:
# Repeat the calculations above,
# but do it for ALL comments,
# not just top level comments.

for comments in submission.comments.list():
    
    try:
        print('total comments:', len(submission.comments.list()))
    except AttributeError:
        pass


not_deleted_comms = 0
deleted_comms=0 
users = {}

for comment in submission.comments.list():
    if comment.author == None:
        deleted_comms += 1
    elif comment.author != None and comment.author not in users:
        users[comment.author] = 1
    elif comment.author != None and comment.author in users:
        users[comment.author] += 1
for comment in submission.comments.list():
    if comment.author != None:
        not_deleted_comms += 1

print("not deleted comments:", not_deleted_comms)
print("deleted comments:", deleted_comms)
print(users)