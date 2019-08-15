from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

    def get_articles(self):
        """
            get all articles of the selected tag
        """
        return self.article_set.filter(is_draft=False).order_by('-created_at')


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=4000)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='articles', default=0)
    is_draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_tags(self):
        """
            get all the tags of an article
        """
        return self.tags.all()
