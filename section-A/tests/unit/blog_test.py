from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):

    def test_create_blog(self):
        b = Blog('Test', 'Test Blog')
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Blog', b.author)
        self.assertListEqual([], b.posts)
    

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        self.assertEqual('Test by Test Author (0 post)', b.__repr__())


    def test_repr__multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts.append('post 01')
        b.posts.append('post 02')
        self.assertEqual('Test by Test Author (2 posts)', b.__repr__())

