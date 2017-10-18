from .models import Article
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

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
    article_list = Article.objects.order_by('-created_at')
    username = request.user.username
    context = { 'article_list': article_list, 'username': username}

    logging.info("user id = "+ request.user.username)
    return render(request, 'blog/index.html', context)

@login_required
def detail(request, article_id):
    logging.info("article_id= "+article_id)
    article_list = Article.objects.order_by('-created_at')[:5]
    article = Article.objects.get(pk=article_id)
    username = request.user.username
    context = { 'article': article, 'username': username, 'article_list': article_list}

    return render(request, 'blog/detail.html', context)

@login_required
def article_add(request):
    username = request.user.username
    article_list = Article.objects.order_by('-created_at')[:5]
    context = {'username': username, 'article_list': article_list}
    return render(request, 'blog/article.html', context)

@login_required
def article_edit(request, article_id):

    article_list = Article.objects.order_by('-created_at')[:5]
    article = Article.objects.get(pk=article_id)
    username = request.user.username
    if article.author == username or username == "admin":
        context = {'article': article, 'username': username, 'article_list': article_list}
        return render(request, 'blog/edit.html', context)
    else:
        error_message = "Edit Fail： sorry, you are not author"
        context = {'error_message': error_message, 'article': article, 'article_list': article_list}
        return render(request, 'blog/detail.html', context)



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
    return HttpResponseRedirect(reverse('blog:index'))


@login_required
def article_delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article_list = Article.objects.order_by('-created_at')[:5]
    username = request.user.username
    if article.author == username or username == "admin":
        article.is_delete = True
        article.save()
        return HttpResponseRedirect(reverse('blog:index'))
    else:
        error_message = "Delete Fail： sorry, you are not author"
        context = {'error_message': error_message, 'article': article, 'article_list': article_list}
        return render(request, 'blog/detail.html', context)


@login_required
def article_save(request):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    new_article = Article(author=author,title=title,content=content)
    new_article.save(force_insert=True)
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
def message_add(request, article_id):
    logging.info("article_id= "+article_id)
    article = Article.objects.get(pk=article_id)
    article_list = Article.objects.order_by('-created_at')[:5]
    username = request.user.username
    context = { 'article': article, 'username': username, 'article_list': article_list}

    return render(request, 'blog/detail.html', context)


@login_required
def message_save(request, article_id):
    author = request.POST['author']
    title = request.POST['title']
    content = request.POST['content']
    article = Article.objects.get(id=article_id)
    article.message_set.create(author=author, title=title, content=content)
    return HttpResponseRedirect(reverse('blog:index'))


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userObj = form.cleaned_data
            username = userObj['username']
            return HttpResponseRedirect(reverse('register_complete'), username)
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def register_complete(request):
    #return HttpResponseRedirect(reverse('login'))
    user = request.user.username
    context = {'user': user}
    return render(request, 'registration/register_complete.html', context)
