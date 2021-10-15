
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


'''
Lab instructions: 
Complete each function below so that all doctests pass.
You can run the doctess with the command
$ python3 -m doctest --verbose lab.py
Once all doctests pass, upload the output of the above command to sakai.
'''

def is_palindrome(s):
    '''
    returns True if a string is the same read forwards and backwards, False otherwise
    HINT:
    Use a specially crafted slice to reverse the string s,
    then check to see if s is equal to its reverse.
    >>> is_palindrome('asdsa')
    True
    >>> is_palindrome('asdasd')
    False
    >>> is_palindrome('taco cat')
    False
    >>> is_palindrome('qwertyuiopoiuytrewq')
    True
    >>> is_palindrome('')
    True
    '''
    return s == s[::-1]


def is_palindrome_number(n):
    '''
    returns True if the digits of the input number form a palindrome
    HINT: 
    convert the number into a string and use your is_palindrome function
    >>> is_palindrome_number(12321)
    True
    >>> is_palindrome_number(123212321)
    True
    >>> is_palindrome_number(1232123)
    False
    '''
    return str(n) == str(n)[::-1]


def string_contains_url(s):
    '''
    A URL is any string that starts with either "http://" or "https://",
    and the URL may be either uppercase or lowercase.
    This function returns whether the input string contains a url
    HINT: 
    use the `in` keyword and the lower() function
    >>> string_contains_url('I love computing for the web :)')
    False
    >>> string_contains_url('The course website is located at https://github.com/mikeizbicki/cmc-csci040')
    True
    >>> string_contains_url('The https protocol is more secure than the http protocol.')
    False
    >>> string_contains_url('My favorite website is http://purple.com')
    True
    >>> string_contains_url('HTTP://SIMPSONSWORLD.COM IS THE BEST. WEBSITE. EVER.')
    True
    >>> string_contains_url('HtTPs://SiMpSoNsWoRld.COM Is tHe BesT. WEBSITE. EVER.')
    True
    '''
    return 'http://' in s.lower() or 'https://' in s.lower()


def extract_TLD(domain):
    '''
    a domain name consists of a series of characters separated by periods;
    the series of letters after the last period is called the top level domain (TLD);
    this function returns the TLD of the input domain
    HINT:
    use the .split() function to "tokenize" the string on the periods
    >>> extract_TLD('www.google.com')
    'com'
    >>> extract_TLD('izbicki.me')
    'me'
    >>> extract_TLD('www.rodong.rep.kp')
    'kp'
    >>> extract_TLD('www.ci.claremont.ca.us')
    'us'
    >>> extract_TLD('research.pizza')
    'pizza'
    '''
    return domain.split('.')[-1]


def remove_duplicate_words(s):
    '''
    This function performs a basic grammar check by removing duplicate words in a string.
    HINT:
    use the split function to "tokenize" the string into a list of words;
    then solve the problem on lists using the `remove_duplicates_from_list` function;
    finally, use the join function to convert the de-duplicated list back into a string
    >>> remove_duplicate_words('please please please please work')
    'please work'
    >>> remove_duplicate_words('this is a a sentence')
    'this is a sentence'
    >>> remove_duplicate_words('if it walks like a duck and talks like a duck, then it is a duck')
    'if it walks like a duck and talks like a duck, then it is a duck'
    >>> remove_duplicate_words('nothing needs to change about this sentence')
    'nothing needs to change about this sentence'
    '''
    a = s.split()
    b = remove_duplicates_from_list(a)
    return ' '.join(b)


def remove_duplicates_from_list(xs):
    '''
    This function is a "helper function" for the remove_duplicate_words function;
    having helper functions is a common pattern in python programming
    HINT:
    step 1: create an empty list;
    step 2: then use a for loop to loop over xs;
    step 3: on each iteration of the for loop, if the value is different than the previous value, then append it to the list you created in step 1
    >>> remove_duplicates_from_list([1,1,2,3,3,1,3,2])
    [1, 2, 3, 1, 3, 2]
    >>> remove_duplicates_from_list([4,2,2,2,2,2,2,3,1,2])
    [4, 2, 3, 1, 2]
    >>> remove_duplicates_from_list([1])
    [1]
    >>> remove_duplicates_from_list([1,1,1,1,1])
    [1]
    >>> remove_duplicates_from_list([])
    []
    '''

    new_list = []
    for i in range(len(xs)):
        if i < len(xs)-1:
            if xs[i] != xs[i+1]:
                new_list.append(xs[i])
        else:
            new_list.append(xs[i])
    return new_list


def how_many_claremonts_in_str(s):
    '''
    returns the number of times the string 'Claremont' appears in s; it is not case sensitive
    HINT:
    there is a built in string function that already implements this method;
    you can find this method listed in the Python Cheatsheet under the section
    "Generic Operations on Containers"
    >>> how_many_claremonts_in_str('This sentence is about Montclair.')
    0
    >>> how_many_claremonts_in_str('This sentence is about Claremont.')
    1
    >>> how_many_claremonts_in_str('THIS SENTENCE IS ABOUT CLAREMONT!')
    1
    >>> how_many_claremonts_in_str('Claremont. Claremont. Claremont. Claremont!')
    4
    >>> how_many_claremonts_in_str('CLAREMONT. claremont. ClaREMonT. Claremont!')
    4
    '''
    return s.lower().count('claremont')
    