import requests as req
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Ask, Job, Show, New
from .forms import UserForms


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
    if request.method == 'POST':
        resp = request.POST.items()
        for key, value in resp:
            pass
        if value == '1':
            for stories in scraper('askstories'):
                created = Ask.objects.get_or_create(
                    by=stories['by'],
                    descendants=stories['descendants'],
                    id=stories['id'],
                    kids=str(stories['kids']) if 'kids' in stories.keys() else None,
                    score=stories['score'],
                    text=stories['text'] if 'text' in stories.keys() else None,
                    time=stories['time'],
                    title=stories['title'],
                    _type=stories['type']
                )
        elif value == '2':
            for stories in scraper('jobstories'):
                created = Job.objects.get_or_create(
                    by=stories['by'],
                    id=stories['id'],
                    score=stories['score'],
                    time=stories['time'],
                    title=stories['title'],
                    _type=stories['type'],
                    url=stories['url'] if 'url' in stories.keys() else None
                )
        elif value == '3':
            for stories in scraper('showstories'):
                created = Show.objects.get_or_create(
                    by=stories['by'],
                    descendants=stories['descendants'],
                    id=stories['id'],
                    kids=str(stories['kids']) if 'kids' in stories.keys() else None,
                    score=stories['score'],
                    text=stories['text'] if 'text' in stories.keys() else None,
                    time=stories['time'],
                    title=stories['title'],
                    _type=stories['type'],
                    url=stories['url'] if 'url' in stories.keys() else None
                )
        elif value == '4':
            for stories in scraper('newstories'):
                created = New.objects.get_or_create(
                    by=stories['by'],
                    descendants=stories['descendants'],
                    id=stories['id'],
                    kids=str(stories['kids']) if 'kids' in stories.keys() else None,
                    score=stories['score'],
                    time=stories['time'],
                    title=stories['title'],
                    _type=stories['type'],
                    url=stories['url'] if 'url' in stories.keys() else None
                )
    else:
        userform = UserForms()
        return render(request, 'myapp/index.html', {'form': userform})
    return HttpResponseRedirect('/')
