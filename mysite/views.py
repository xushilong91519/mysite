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

def search(request):
    template=get_template('mysite/index.html')
    str_list=[re.compile(x) for x in request.GET['kw'].split()]
    d={}
    for p in Post.objects.all():
        for tmp in str_list:
            if re.search(tmp,p.body):
                try:
                    d[p]+=1
                except:
                    d[p]=1
    posts=sorted(d.keys(),key=lambda a:d[a],reverse=True)
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)
