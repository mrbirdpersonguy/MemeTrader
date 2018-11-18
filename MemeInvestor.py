# ---------------------------
# bot login information
# username: shartvix
# pw: lamp$screen%eye!goat7dr
# ---------------------------

import praw
import time


def invest_in_memes():

    # reddit api login
    r = praw.Reddit(client_id='PNB7w59N7hGO-g',
                    client_secret='nsX1E3v3vTsAW9fdpVK8jtwCFFo',
                    username='shartvix',
                    password='lamp$screen%eye!goat7dr',
                    user_agent='shartingvix and trading memes')

    meme_investor_bot = r.redditor('MemeInvestor_bot')

    # list of memes already invested in
    meme_coin_balance = 0
    invested_memes = []

    # the subreddit shartvix will live on
    sr = r.subreddit('memeeconomy')

    for submission in sr.stream.submissions():
        post_time = submission.created_utc
        if (time.time() - post_time) < 1000 and submission.upvote_ratio >= .8 \
                and submission.score >= 5:
            print(submission.title)
            for comment in submission.comments:
                if comment.author == meme_investor_bot:
                    print(comment.author)
                    comment.reply("!balance")

invest_in_memes()

