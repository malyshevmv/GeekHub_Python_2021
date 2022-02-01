import requests as req
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Ask, Job, Story


def scraper(category):
    lst_category = ['askstories', 'showstories', 'newstories', 'jobstories']
    if category not in lst_category:
        yield 'The selected category does not exist'
    url = f'https://hacker-news.firebaseio.com/v0/{category}.json?print=pretty'
    id_stories = req.get(url)
    lst_id_stories = id_stories.json()
    for id_stories in lst_id_stories:
        url_api = 'https://hacker-news.firebaseio.com/v0/item/'
        url_stories = f'{id_stories}.json?print=pretty'
        r = req.get(url_api + url_stories)
        res = r.json()
        yield res


def index(request):
    return render(request, 'myapp/index.html')


def create(request):
    if request.method == 'POST':
        selected_value = request.POST.get('value')
        if selected_value == 'Ask':
            for stories in scraper(selected_value):
                Ask.by = stories['by']
                Ask.id = stories['id']
                Ask.text = stories['text']
                Ask.title = stories['title']
                Ask.save()
        elif selected_value == 'Job':
            for stories in scraper(selected_value):
                Job.by = stories['by']
                Job.id = stories['id']
                Job.text = stories['text']
                Job.title = stories['title']
                Job.save()
        elif selected_value == 'Story':
            for stories in scraper(selected_value):
                Story.by = stories['by']
                Story.id = stories['id']
                Story.text = stories['text']
                Story.title = stories['title']
                Story.save()
    return HttpResponseRedirect('/')
