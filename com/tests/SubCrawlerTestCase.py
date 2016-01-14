import unittest
from com.crawler.SubCrawler import has_video_url, generate_data_structure, split_text


class SubCrawlerTestCase(unittest.TestCase):
    def test_presence_youtube_video_in_itself(self):
        self.assertTrue(has_video_url(
            "https://www.youtube.com/watch?v=mlzrhbpmyai, http://www.twitch.tv/esl_lol/v/30574431?t=5h09m40s  "))

    def test_presence_twitch_video(self):
        self.assertTrue(has_video_url(
            "http://www.twitch.tv/esl_lol/v/30574431?t=5h09m40s , https://www.youtube.com/watch?v=mlzrhbpmyai  "))

    def test_split_text(self):
        self.assertEquals(len(split_text("* **format:**\n" +
                                         "* **6 teams:**")), 2)

    def test_generate_any_json(self):
        data_struct = generate_data_structure(
            'a2| **qg** [](#qg) |vs.| [](#dig) **dig** | [picks &amp; bans]'
            '(http://www.twitch.tv/esl_lol/v/30574431?t=1h47m41s) | '
            '[game start](http://www.twitch.tv/esl_lol/v/30574431?t=1h57m05s)'
            ' | [picks &amp; bans](https://www.youtube.com/watch?v=ytsjecr73nk)'
            ' | [game start](https://www.youtube.com/watch?v=ytsjecr73nk&t=7m45s)'
            ' | [highlights](https://www.youtube.com/watch?v=j67z3z9gnsc)'
            ' |', 'title')
        self.assertIsNotNone(data_struct)

    def test_generate_teams(self):
        data_struct = generate_data_structure(
            'a2|'
            ' **qg** [](#qg) |'
            'vs.|'
            ' [](#dig) **dig** |'
            ' [picks &amp; bans](http://www.twitch.tv/esl_lol/v/30574431?t=1h47m41s) |'
            ' [game start](http://www.twitch.tv/esl_lol/v/30574431?t=1h57m05s) |'
            ' [picks &amp; bans](https://www.youtube.com/watch?v=ytsjecr73nk) |'
            ' [game start](https://www.youtube.com/watch?v=ytsjecr73nk&t=7m45s) |'
            ' [highlights](https://www.youtube.com/watch?v=j67z3z9gnsc) |',
            'title')
        self.assertTrue('qg' in data_struct['blue_team'])
        self.assertTrue('dig' in data_struct['red_team'])
        self.assertTrue('a2' in data_struct['local_id'])
        self.assertIsNotNone(data_struct['pick_ban'])
        self.assertIsNotNone(data_struct['pick_ban']['twitch'])
        self.assertIsNotNone(data_struct['pick_ban']['youtube'])
        self.assertIsNotNone(data_struct['game_start'])
        self.assertIsNotNone(data_struct['game_start']['youtube'])
        self.assertEqual(data_struct['game_start']['youtube'],
                         ' [game start](https://www.youtube.com/watch?v=ytsjecr73nk&t=7m45s) ')
        self.assertIsNotNone(data_struct['highlights'])

        if __name__ == '__main__':
            unittest.main()
