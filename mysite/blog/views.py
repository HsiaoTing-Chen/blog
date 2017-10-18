from .models import Article
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


import logging
import logging.config
import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)

@login_required
def index(request):
    article_list = Article.objects.order_by('-created_at')[:5]
    username = request.user.username
    context = { 'article_list': article_list, 'username': username }

    logging.info("user id = "+ request.user.username)
    return render(request, 'blog/index.html', context)

@login_required
def detail(request, article_id):
    logging.info("article_id= "+article_id)
    article = Article.objects.get(pk=article_id)
    context = { 'article': article, }

    return render(request, 'blog/detail.html', context)

@login_required
def article_add(request):

    return render(request, 'blog/article.html')

@login_required
def article_edit(request, article_id):
    # article_list = get_object_or_404(Article, id=article_id)
    logging.info("article_id= "+article_id)
    article = Article.objects.get(pk=article_id)
    context = { 'article': article, }

    return render(request, 'blog/edit.html', context)

@login_required
def article_edit_save(request, article_id):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    article = Article.objects.get(pk=article_id)
    article.author = author
    article.title = title
    article.content = content
    article.save()
    logging.info(author+" , "+title+" , "+content)
    return HttpResponseRedirect(reverse('blog:index'))


@login_required
def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.is_delete = True
    article.save()
    return HttpResponseRedirect(reverse('blog:index'))


@login_required
def article_save(request):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    new_article = Article(author=author,title=title,content=content)
    new_article.save(force_insert=True)

    logging.info(author+" , "+title+" , "+content)
    return HttpResponseRedirect(reverse('blog:index'))


@login_required
def article_save(request):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    new_article = Article(author=author,title=title,content=content)
    new_article.save(force_insert=True)

    logging.info(author+" , "+title+" , "+content)
    return HttpResponseRedirect(reverse('blog:index'))


def message_add(request, article_id):
    #article_list = get_object_or_404(Article, id=article_id)

    logging.info("article_id= "+article_id)
    article = Article.objects.get(pk=article_id)
    context = { 'article': article, }

    return render(request, 'blog/detail.html', context)


def message_save(request, article_id):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    article = Article.objects.get(id=article_id)
    # create a new message
    article.message_set.create(author=author, title=title,content=content)
    return HttpResponseRedirect(reverse('blog:index'))
    # return HttpResponseRedirect(reverse('blog:detail',args=(article.id,)))

"""
def login(request):
    if request.user.is_authenticated():
        #return HttpResponseRedirect('/hello/')
        return HttpResponseRedirect(reverse('blog:index',args=(user,)))

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    logging.info(username+"/"+password)
    user = auth.authenticate(username=username, password=password)

    if  user is not None and user.is_active:
        auth.login(request, user) # maintain the state of login
        #return HttpResponseRedirect('/hello/')
        return HttpResponseRedirect(reverse('blog:index',args=(user,)))
    else:
        return HttpResponseRedirect(reverse('blog:index'))


def logout(request):
    username = request.user.username
    context = { 'username': username }
    return render(request, 'blog/logout.html', context)
"""
