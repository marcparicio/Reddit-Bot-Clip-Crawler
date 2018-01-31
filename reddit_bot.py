import praw
import config
import requests

def main():
    reddit = bot_login()

    subreddit = reddit.subreddit('livestreamfail')
    for submission in subreddit.stream.submissions():
        process_submission(submission)

def bot_login():
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "livestreamfail clip crawler v0.1")

    return reddit

def process_submission(submission):
    submission_url = submission.url
    if (submission_url is not None):
        if "https://clips.twitch.tv/" in submission_url:
            slug = submission_url.rsplit('/',1)[-1]
            print ("New submission found with slug: " + slug)
            print ("Submitting clip...")
            submit_slug(slug)

def submit_slug(slug):
    url = "http://livestream-highlights.herokuapp.com/clips?slug=" + slug
    requests.post(url)
    print ("Clip submitted successfully!")

if __name__ == '__main__':
    main()
