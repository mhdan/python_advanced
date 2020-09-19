from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def index(request):
    all_posts = Post.objects.all()
    ret_html = '<body>'
    for each_post in all_posts:
        ret_html += '<p>' + each_post.text + '</p>'
    ret_html += '</body>'

    return HttpResponse(ret_html)
