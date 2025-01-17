from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, User
from .forms import SearchForm
from .forms import ArticleForm

def index(request):
    searchForm = SearchForm(request.GET)
    user = get_object_or_404(User,pk=1)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
        'message': 'Welcome my BBS',
        'articles': articles,
        'searchForm': searchForm,
        'user': user,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def new(request):
    articleForm = ArticleForm()

    context = {
        'message': 'New Article',
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context)
    
def create(request):
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()

    context = {
        'message': 'Create article ' + str(article.id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def edit(request, id):
    article = get_object_or_404(Article, pk=id)
    articleForm = ArticleForm(instance=article)
    context = {
        'message': 'Edit Article ' + str(id),
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context)


def update(request, id):
    if request.method =='POST' :
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST,instance=article)
        if articleForm.is_valid():
            articleForm.save()
    context = {
        'message': 'Show Article ' + str(id),
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()

    articles = Article.objects.all()
    context = {
        'message': 'Delete article ' + str(id),
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context)
