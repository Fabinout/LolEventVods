import praw
import re
import json


def extract_submissions():
    r = praw.Reddit('PRAW related-question monitor by /u/_Daimon_ v 1.0. '
                    'Url: https://praw.readthedocs.org/en/latest/'
                    'pages/writing_a_.html')
    r.login(username="crawlerVOD", password="laforce")
    already_done = []
    subreddit = r.get_subreddit('LoLeventVoDs')
    hot_topics = subreddit.get_hot(limit=50)
    for submission in hot_topics:
        if submission.author.name == "LoLeventVoDs":
            print(submission.title)
            #     print()
            # print(submission.selftext.lower())


def has_video_url(string):
    return re.search("(www\.youtube\.com)|(www\.twitch\.tv)", string)


def split_text(string):
    return string.split("\n")


def generate_data_structure(param):
    data = {'full_text': param}
    tokens = param.split("|")
    data['local_id'] = tokens[0]
    data['blue_team'] = tokens[1]
    data['red_team'] = tokens[3]
    data['pick_ban'] = {'twitch': tokens[4], 'youtube': tokens[6]}
    return data


def to_json(data):
    json_dumps = json.dumps(data)
    return json_dumps
