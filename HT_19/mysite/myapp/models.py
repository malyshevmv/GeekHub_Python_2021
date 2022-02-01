from django.db import models


class Ask(models.Model):
    by = models.CharField('by', max_length=50, default='NAME')
    id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=250)
    title = models.CharField(name='title', max_length=50)

    def __str__(self):
        return self.by


class Job(models.Model):
    by = models.CharField('by', max_length=50, default='NAME')
    id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=250)
    title = models.CharField(name='title', max_length=50)

    def __str__(self):
        return self.by


class Story(models.Model):
    by = models.CharField('by', max_length=50, default='NAME')
    id = models.IntegerField(primary_key=True)
    text = models.TextField(max_length=250)
    title = models.CharField(name='title', max_length=50)

    def __str__(self):
        return self.by

    