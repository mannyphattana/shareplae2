from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Word(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    esearch = models.TextField()
    eentry = models.TextField()
    tentry = models.TextField()
    ecat = models.TextField()
    ethai = models.TextField(null=True)
    esyn = models.TextField(null=True)
    eant = models.TextField(null=True)

    def __str__(self):
        return self.eentry

    def get_absolute_url(self):
        return reverse('word-detail', args=[str(self.id)])


class Comment(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    ts = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    word = models.ForeignKey(Word, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
