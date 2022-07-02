from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here.


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(data):
        # Create a user
        user_1 = User.objects.create_user(
            username="david", password="admin123")
        user_1.save()

        # Create blog
        post_1 = Post.objects.create(
            author=user_1, title="Test Features", body="This is a test..")
        post_1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "david")
        self.assertEqual(title, "Test Features")
        self.assertEqual(body, "This is a test..")
