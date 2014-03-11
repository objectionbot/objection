
print ('Starting program...')
import time
import praw
import random
import re
print ('The current date and time is ' + time.strftime("%X"))
print (time.strftime("%X") + ': Imported successfully!')


# Login in to Reddit and the bot
print (time.strftime("%X") + ': Logging into reddit...')
r = praw.Reddit('objectionbot')
r.login("objectionbot","jakey123") 
already_done = set()
print (time.strftime("%X") + ': Successfully logged in!')
prawWords = ['a', 'e', 'i', 'o', 'u']


#Find comment to tip
def pick_random_comment():

    subreddit = r.get_subreddit('all')
    print (time.strftime("%X") + ': Getting comments...')
    subreddit_comments = subreddit.get_comments(limit=200)
    print (time.strftime("%X") + ': Comments received!')
    for comment in subreddit_comments:
        op_text = comment.body
        has_praw = any(string in op_text for string in prawWords)
        if comment.id not in already_done and has_praw:
            comment.reply('http://i.imgur.com/HZRC63c.jpg')
            print (time.strftime("%X") + ': Objection has been posted.')
            already_done.add(comment.id)
            break
