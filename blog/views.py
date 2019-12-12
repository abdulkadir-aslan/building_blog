from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category,Tag


def index(request):
    context = dict()
    context['items'] = Category.objects.filter(
        status='published'
    ).order_by('title')
    
    return render(request, "index.html", context)

def category(request, cat_slug):
    context = dict()
    category = Category.objects.get(slug=cat_slug)
    context['category'] = category
    context['post']=Post.objects.all()
    context['items'] = Post.objects.filter(
        category=category,
        status='published'
    ).order_by('-created_at')
    return render(request, 'post.html', context)


