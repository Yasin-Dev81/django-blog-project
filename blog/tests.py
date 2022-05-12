from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .views import BlogPost


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username='user1')
        cls.post1 = BlogPost.objects.create(
            title='blog post 1',
            text='for testing1',
            status=BlogPost.STATUS_CHOICES[0][0],  # published
            author=user1
        )
        cls.post2 = BlogPost.objects.create(
            title='blog post 2',
            text='for testing2',
            status=BlogPost.STATUS_CHOICES[0][1],  # draft
            author=user1
        )

    def test_blog_list_url(self):
        response = self.client.get('blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_list_url_name(self):
        response = self.client.get(reverse('blog_list_url'))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_post1(self):
        response = self.client.get(reverse('blog_list_url'))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)

    # def test_blog_list_post2(self):
    #     response = self.client.get(reverse('blog_list_url'))
    #     self.assertContains(response, self.post2.title)
    #     self.assertContains(response, self.post2.text)
    #     self.assertContains(response, self.post2.author)

    def test_blog_details_status_code_post1(self):
        response = self.client.get(reverse('blog_detail_url', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_post1(self):
        response = self.client.get(reverse('blog_detail_url', args=[self.post1.id, ]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.author)

    def test_blog_detail_status_code_post2(self):
        response = self.client.get(reverse('blog_detail_url', args=[self.post2.id, ]))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail_post2(self):
        response = self.client.get(reverse('blog_detail_url', args=[self.post2.id, ]))
        self.assertContains(response, self.post2.title)
        self.assertContains(response, self.post2.text)
        self.assertContains(response, self.post2.author)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('blog_detail_url', args=[999]))
        self.assertEqual(response.status_code, 404)

