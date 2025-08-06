import os
from django.http import HttpResponse, FileResponse
from django.template import loader
from django.db.models import Q
from .models import News
from config import settings

def news(request):
    news_list = News.objects.order_by('-date').values()[:10]
    template = loader.get_template('news.html')
    context = {
        'news': news_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    try:
        news = News.objects.get(id=id)
    except:
        template = loader.get_template('404.html')
        return HttpResponse(template.render())
    
    template = loader.get_template('details.html')

    tags = news.tags.split(' ')
    context = {
        'post': news,
        'tags': tags,
    }

    session_key = f'viewed_news_{news.id}'
    if not request.session.get(session_key, False):
        news.views += 1
        news.save()
        request.session[session_key] = True

    return HttpResponse(template.render(context, request))



def category(request, tag):
    data = News.objects.filter(tags__startswith=tag).order_by('-date')
    if len(data) < 10:
        data = News.objects.filter(tags__contains=tag).order_by('-date')

    template = loader.get_template('category.html')
    context = {
        'name': tag,
        'news': data,
    }
    return HttpResponse(template.render(context, request))


def pdf(request, id):
    file = f"{id}.pdf"
    try:
        pdf_path = os.path.join(settings.BASE_DIR, 'news', 'templates', file)
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    except:
        template = loader.get_template('404.html')
        return HttpResponse(template.render())