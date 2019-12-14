from blog.models import Category,Tag


def navbar(request):
    return{'categories':Category.objects.filter(status="published")}