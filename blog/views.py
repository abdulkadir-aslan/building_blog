from django.shortcuts import render,get_object_or_404, redirect
from blog.models import Post,Category,Tag
from django.contrib import messages

def index(request,tag_slug=None):
    context = dict()
    context['items'] = Post.objects.filter(status='published').order_by('-create_at')
    if tag_slug:
        category = Category.objects.get(slug=tag_slug)
        context['category']=category
        # print(category.user_viewed())  artis miktarini cmd ekraninda gosterir
        category.user_viewed()
        context['items']= context['items'].filter(category=category)
    return render(request, "index.html", context)

def tag_post(request,tag_slug,post_slug):
    context = dict()
    context['item']= Post.objects.get(slug=post_slug)
    context['item'].user_viewed() #postu her yeniledigimizde veri tabaninda degerini bir arttirir
    context['items']= Post.objects.filter(status='published').order_by('-create_at')
    return render(request,'post.html',context)

def cat_added(request):
    if request.method =='POST':
        if request.user.is_staff:
            r_post=request.POST
            title = r_post.get('title')            
            try:              
                item=Category.objects.create(
                    title = title,
                    slug = title,
                )
                messages.add_message(
                    request, messages.SUCCESS, 
                    f'{title} Kaydedildi'
                )
                if request.user.is_superuser:
                    item.status = 'published'
                    item.save()
                    messages.add_message(
                        request,messages.SUCCESS,
                        f'{title} Yayinlandi'
                    )
                return redirect('home')
            except:
                messages.add_message(
                    request,messages.WARNING,
                    f'{ title } kaydedilemedi'
                )
    return render(request,'user_blog/cat_added.html',{})
