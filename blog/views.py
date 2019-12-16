from django.shortcuts import render,get_object_or_404, redirect
from blog.models import Post,Category,STATUS
from django.contrib import messages
from .forms import CategoryForm,CategoryModelForm
from django.contrib.auth.models import Group




def index(request,tag_slug=None):
    context = dict()
    context['forms'] = CategoryModelForm()
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
    context = {'form':CategoryForm() }
    if request.method =='POST':
        if request.user.is_staff:
            # r_post=request.POST
            # print(r_post)
            # title = r_post.get('title')   
            # print(title) 
            form = CategoryForm(request.POST)        
            title  = form.data.get('title')
            try:              
                item=Category.objects.create(
                    title = title,
                    slug = title,
                    user = request.user,
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
            except Exception:
                print(Exception)
                messages.add_message(
                    request,messages.WARNING,
                    f'{ title } kaydedilemedi'
                )
    return render(request,'user_blog/cat_added.html',context)


def  cat_list(request):
    context = dict()
    grp = Group.objects.get(name='BlogAdmin')
    categories = Category.objects.all()
    context = {
        'cat_list': categories,
        # 'is_superuser': request.user.is_superuser --<<>>kullanici superuser oldugunda listeyi gorebiliyordu
        'is_admin':grp in request.user.groups.all()  #burada kullanici grp icinde oldugunda gorebilecek
    }
    return render(request,'user_blog/cat_list.html',context)


    
#categorilein yayinladi veya silindi olrak gorulmesi icin yazdigimiz fonksiyon
def category_update_status(request,cat_id,status):
    st =[item[0] for item in STATUS]
    if not status in st:
        return redirect('cat_list')
    istance = Category.objects.get(id=cat_id)
    istance.status = status
    istance.save()
    messages.add_message(request,messages.SUCCESS,f"{istance.title} Silindi")
    return redirect('cat_list')