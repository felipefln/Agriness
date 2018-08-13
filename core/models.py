from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    DRAFT = 1
    PUBLISHED = 2
    OPTIONS = {
        DRAFT: 'Draft',
        PUBLISHED: 'Published'
    }
    CHOICES = tuple(OPTIONS.items())

    title = models.CharField(max_length=254)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(default=DRAFT, choices=CHOICES)
    category = models.ManyToManyField(Category, related_name='article_list')
    creation_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == self.PUBLISHED:
            self.publish_date = timezone.now()
        super(Article, self).save(*args, **kwargs)
