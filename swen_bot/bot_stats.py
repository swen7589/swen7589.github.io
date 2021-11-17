import praw
import pprint

# FIXME:
# login to reddit with your bot's credentials;
# recall that this requires creating a praw.ini file
# 
# WARNING:
# If you include any credential information in your final submission,
# you will receive NEGATIVE POINTS on your lab!!!
reddit = praw.Reddit('bot', user_agent='swen_bot')

# connect to the "Main Discussion Thread" reddit submission
submission = reddit.submission(url='https://old.reddit.com/r/BotTown/comments/qqmr8l/main_discussion_thread/')

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


print('='*40)
print('top level comments')
print('='*40)

# 1 and 2
non_deleted_top_comms = []
deleted_top_comms = []

if comment in reddit.submission.comments:
    non_deleted_top_comms.append(comment)
    print('top comments:', len(non_deleted_top_comms))
else:
    deleted_top_comms.append(comment)
    print('deleted top comments:', len(deleted_top_comms))

# 3
each_user_comms = []

if user in reddit.submission.users:
    each_user_comms.append(user)
    print('comments by users:', len(each_user_comms))

# FIXME:
# Repeat the calculations above,
# but do it for ALL comments,
# not just top level comments.


print('='*40)
print('all comments')
print('='*40)


all_comms = []

if comment in reddit.submission:
    all_comms.append(comment)
    print('all comments:', len(all_comms))

if comment in reddit.submission.comments:
    non_deleted_top_comms.append(comment)
    print('top comments:', len(non_deleted_top_comms))
else:
    deleted_top_comms.append(comment)
    print('deleted top comments:', len(deleted_top_comms))


