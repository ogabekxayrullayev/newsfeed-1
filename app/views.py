from django.shortcuts import render, get_object_or_404
from app.models import News, Category

def news(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list":  news_list
    }
    
    
    return render(request, 'news/news_list.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news":news
    }
    return render(request, "news/news_detail.html", context )

def homePageView(request):
    news  = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        "categories":categories,
    }
    
    return render(request, 'news/index.html', context)