from unittest import TestCase
from post import Post


class PostTest(TestCase):

    def test_create_post(self):
        p = Post('test', 'test Content')
        self.assertEqual('test', p.title)
        self.assertEqual('test Content', p.content)


    def test_json(self):
        p = Post('test', 'test Content')
        excepted = {'title' : p.title, 'content' : p.content}
        self.assertDictEqual(excepted, p.json())