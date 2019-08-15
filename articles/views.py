from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from django.contrib.auth.decorators import login_required

from .models import Article, Tag


def home(request):
    """
        Home page. Displays all the articles and drafts.
    """
    # get published articles
    articles = Article.objects.filter(is_draft=False).order_by('-created_at')

    # get all drafts
    created_by = 0
    if request.user.is_authenticated:
        created_by = request.user

    drafts = Article.objects.filter(
        created_by=created_by, is_draft=True).order_by('-created_at')

    # get top three tags
    popular_tags = Tag.objects.filter(article__is_draft=False).annotate(
        article_count=models.Count('article')).order_by('-article_count')[:3]

    return render(request, 'home.html', {'articles': articles, 'drafts': drafts, 'popular_tags': popular_tags})


@login_required
@csrf_exempt
def new_article(request):
    """
        Create new Article.
    """
    if request.method == 'POST':
        # save the article object first
        article = Article(
            title=request.POST['title'], content=request.POST['content'], created_by=request.user, is_draft=request.POST['is_draft'].title())
        article.save()

        # get all the user input tags
        tag_string = request.POST['tags']
        tag_list = tag_string.replace(' ', '').split(',')

        # loop through every tag
        for _tag in tag_list:
            # check if tag already exists in the db
            tag = Tag.objects.filter(name=_tag).first()
            if tag:
                # add the existing tag
                article.tags.add(tag)
            else:
                # create and add new tag
                article.tags.create(name=_tag)

        return redirect('/')
    return render(request, 'new_article.html')


def tag_articles(request, pk):
    """
        display all articles of the selected tag
    """
    tag = Tag.objects.get(id=pk)
    articles = tag.get_articles()
    return render(request, 'tag_articles.html', {'tag': tag, 'articles': articles})
