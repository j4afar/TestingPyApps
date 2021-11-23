from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):


    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Blog')
        b.posts.append(Post('test title','my content'))
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].content, 'my content')
        self.assertEqual(b.posts[0].title, 'test title')


    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        excepted = {
            'title' : 'Test',
            'author' : 'Test Author', 
            'posts' : [{'title':'Test Post', 'content': 'Test Content'}]
        }
        
        self.assertDictEqual(excepted, b.json())