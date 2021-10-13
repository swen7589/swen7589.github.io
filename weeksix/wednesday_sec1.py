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

# these are the term counts calculated in the lab
lab_dict = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

terms = lab_dict.keys()
counts = lab_dict.values()

# this code generates a plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(terms, counts)
plt.show()
