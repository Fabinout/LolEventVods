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
            lines = split_text(submission.selftext)
            for line in lines:
                if has_video_url(line):
                    print(line)
                    generate_data_structure(line, submission.title)


def has_video_url(string):
    return re.search("(www\.youtube\.com).*(www\.twitch\.tv)", string)


def split_text(string):
    return string.split("\n")


def generate_data_structure(param, title):
    data = {'full_text': param}
    tokens = param.split("|")
    data['title'] = title
    data['local_id'] = tokens[0]
    data['blue_team'] = tokens[1]
    data['red_team'] = tokens[3]
    data['pick_ban'] = {'twitch': tokens[4], 'youtube': tokens[6]}
    data['game_start'] = {'twitch': tokens[5], 'youtube': tokens[7]}
    data['highlights'] = tokens[8]

    return data


def write_json_file(data_struct):
    name_file = data_struct.title + '_' + data_struct['local_id']
    with open('com/resources/' + name_file, 'w') as f:
        f.write(to_json(data_struct))
        f.close()


def to_json(data):
    json_dumps = json.dumps(data)
    return json_dumps
