from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .models import Post
import re
# Create your views here.

def homepage(request):
    template=get_template('mysite/index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def showpost(request,Slug):
    template=get_template('mysite/post.html')
    try:
        post=Post.objects.get(slug=Slug)
        if post:
            post.number+=1
            post.save()
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return HttpResponse('ERROR:Page Not Found.')

def homepage_sorted(request,order):
    template=get_template('mysite/index.html')
    posts=Post.objects.order_by('-'+order).all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)

def search(request,sentence):
    str_list=[re.complie(x) for x in sentence.split()]
    posts=[]
    for p in Post.objects.all():

