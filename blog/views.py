from django.shortcuts import render,get_object_or_404
from blog.models import Post,Category,Tag


def index(request,tag_slug=None):
    context = dict()
    context['items'] = Post.objects.filter(status='published').order_by('-create_at')
    if tag_slug:
        category = Category.objects.get(slug=tag_slug)
        context['category']=category
        context['items']= context['items'].filter(category=category)
    return render(request, "index.html", context)

def tag_post(request,tag_slug,post_slug):
    context = dict()
    context['item']= Post.objects.get(slug=post_slug)
    context['item'].user_viewed() #postu her yeniledigimizde veri tabaninda degerini bir arttirir
    context['items']= Post.objects.filter(status='published').order_by('-create_at')
    return render(request,'post.html',context)



