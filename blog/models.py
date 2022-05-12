from django.db import models
from django.shortcuts import reverse


class BlogPost(models.Model):
    # title
    title = models.CharField(max_length=100)
    # text
    text = models.TextField()
    # author
    author = models.ForeignKey('auth.User', models.CASCADE)
    # date
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_edited = models.DateTimeField(auto_now=True)
    # status: published, draft
    STATUS_CHOICES = (('pub', 'Published'), ('drf', 'Draft'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return '%s [from %s]' % (self.title, self.author)

    def get_absolute_url(self):
        return reverse('blog_detail_url', args=[self.id, ])
