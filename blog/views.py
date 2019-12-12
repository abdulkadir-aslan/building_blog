from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category,Tag


def index(request):
    context = dict()
    context['items']=Post.objects.all()
    return render(request, "index.html", context)

