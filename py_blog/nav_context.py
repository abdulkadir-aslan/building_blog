from blog.models import Category,Tag
from django.contrib.auth.models import Group

def navbar(request):
    return{'categories':Category.objects.filter(status="published")}




def user_is_admin_func(request):   #Burada yaptigimiz grup un butun sayfalarda gorunmesini saglamak
    grp = Group.objects.get(name='BlogAdmin')
    return {
        'user_is_admin': grp in request.user.groups.all()   
    }