from django.db import models

STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','silindi'),
]
DEFAULT_STATUS ="draft"

class Category(models.Model):
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True)
    content = models.TextField()
    status= models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    


class Post(models.Model):
    categories = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='post',blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    is_home = models.BooleanField(default=False) 
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


