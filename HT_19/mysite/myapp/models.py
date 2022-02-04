from django.db import models


class Ask(models.Model):
    by = models.CharField('by', max_length=50, default=None)
    descendants = models.IntegerField(default=None)
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(max_length=250, default=None, null=True)
    score = models.IntegerField(default=None)
    text = models.TextField(default=None, null=True)
    time = models.IntegerField(default=None)
    title = models.CharField(name='title', max_length=50)
    _type = models.TextField(max_length=250, default=None)
    objects = models.Manager()

    def __str__(self):
        return self.by


class Job(models.Model):
    by = models.CharField('by', max_length=50, default='NAME_JOB')
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(default=None)
    time = models.IntegerField(default=None)
    title = models.CharField(name='title', max_length=50)
    _type = models.TextField(max_length=250, default=None, null=True)
    url = models.URLField(default=None, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.by


class Show(models.Model):
    by = models.CharField('by', max_length=50, default=None)
    descendants = models.IntegerField(default=None)
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(max_length=250, default='kids', null=True)
    score = models.IntegerField(default=None)
    text = models.TextField(default='text', null=True)
    time = models.IntegerField(default=None)
    title = models.CharField(name='title', max_length=50)
    _type = models.TextField(max_length=250, default=None, null=True)
    url = models.URLField(default=None, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.by


class New(models.Model):
    by = models.CharField('by', max_length=50, default='NAME_NEW')
    descendants = models.IntegerField(default=0, null=True)
    id = models.IntegerField(primary_key=True)
    kids = models.TextField(max_length=250, default='kids', null=True)
    score = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    title = models.CharField(name='title', max_length=50, default=None, null=True)
    _type = models.TextField(max_length=250, default='TYPE', null=True)
    url = models.URLField(default=None, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.by
