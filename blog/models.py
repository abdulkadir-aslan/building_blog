from django.db import models

STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','silindi'),
    
]
DEFAULT_STATUS ="draft"  #defaut deger olrak verildigi icin isaretleme olmadiginda Taslak olarak goster

class Category(models.Model):
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True)
    content = models.TextField()
    status= models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(max_length=100,blank=True,unique=True)
    status = models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at  =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='post',blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    is_home = models.BooleanField(default=False) 
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    



#blank=True ->Alan bo; birakilabilir
#blank=False->Alan doldurulmak zorunda
##choices->Bu alan için seçenek olarak kullanmak üzere tam olarak iki öğeden oluşur
#Her bağlantıdaki ilk öğe, modelde ayarlanacak gerçek değer ve ikinci öğe de insan tarafından okunabilen addır7
#YEAR_IN_SCHOOL_CHOICES = [
    # ('FR', 'Freshman'),
    # ('SO', 'Sophomore'),]
