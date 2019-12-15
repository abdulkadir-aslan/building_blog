from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','silindi'),
    
]
DEFAULT_STATUS ="draft"  #defaut deger olrak verildigi icin isaretleme olmadiginda Taslak olarak goster

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True)
    content = models.TextField()
    status= models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    viewed = models.PositiveIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def user_viewed(self):
        self.viewed +=1
        self.save() 
        return f"{self.viewed}"

    def get_absolute_url(self):
    #     return f"/category/{self.slug}/"
        return reverse('cat', kwargs={'tag_slug':self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(max_length=100,blank=True,unique=True)
    status = models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at  =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
    #     return f"/category/{self.slug}/"
        return reverse('cat', kwargs={'tag_slug':self.slug})


class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags = models.ForeignKey(Tag,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150,blank=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='post',blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default=DEFAULT_STATUS)
    viewed = models.PositiveIntegerField(default=0) #post modelinde artis sayisini gosteren field
    is_home = models.BooleanField(default=False) 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title   #+":"+ self.content  bu ozellik titledan sonra content i de gosteriyor
    
    def user_viewed(self): #yenileme degerini 1 arttiran method
        self.viewed +=1
        self.save()
        return f"{self.viewed}"
    
    
    def get_absolute_url(self):

        return reverse('post',kwargs={'tag_slug':self.category.slug,'post_slug':self.slug})
    
    
    def  get_latest_post(self): #son bes postu gosteriyor
        latest_post= Post.objects.filter(category=self.category,status='published').exclude(id=self.id)[:5]
        return latest_post


#blank=True ->Alan bo; birakilabilir
#blank=False->Alan doldurulmak zorunda
##choices->Bu alan için seçenek olarak kullanmak üzere tam olarak iki öğeden oluşur
#Her bağlantıdaki ilk öğe, modelde ayarlanacak gerçek değer ve ikinci öğe de insan tarafından okunabilen addır7
#YEAR_IN_SCHOOL_CHOICES = [
    # ('FR', 'Freshman'),
    # ('SO', 'Sophomore'),]


##ORM AYARLRI
    # Post.objects.all()->Butun postlari gosterir
    # Post.objects.get(title="Ali")->postun icinde title ali olani getirir yoksa hata verir
    # Post.objects.filter(title__contains="Ti")->postun titlenin icinde Ti harfi olnlari getirir
#     Post.objects.bulk_create([
# ...  Post(name='spike', email='spike@mail.com'),
# ...  Post(name='tyke', email='tyke@mail.com'),        -.>bulk_create  Bir kerede birden fazla post olusturmaya yarar
# ...  Post(name='droopy', email='droopy@mail.com'),
# ... ])
    # Post.objects.filter(title__contains="ke")->contains buyuk kucuk harf duyarlidir /icontains duyarli degildir
    # Post.objects.filter(title__startswith="t")->Pastun icinde ilk harfi 't' ile baslayan title lari gosterir
    # Post.objects.filter(title__endswith="o")->postun icinde son harfi 'o ' ile biten title lari gosterir
    # Post.objects.filter(id__gt=0)-> post icinden id si 0 ' dan sonra gelenleri goster
    # filter() yöntemi döndürür QuerySet bazen sadece tablodan tek bir kayıt getirmesini istediğiniz. 
    # Bu durumları ele almak için objects yönetici bir get()yöntem sağlar.
    #  get()Yöntem ile aynı parametreleri kabul eder filter()yöntemi ancak yalnızca tek bir nesneyi geri gönderir. 
    # get() Birden fazla nesne bulursa, bir "MultipleObjectsReturned" istisna oluşturur. 
    # Herhangi bir nesne bulamazsa "DoesNotExististisna" yaratır .
    # filter() da ise bos doner hata vermez.
    # Post.objects.order_by("-title")->title a gore ters sirala ->title olsydi normal siralayacakti
    # Post.objects.filter(title__contains='foo').order_by("title")->title da 'foo ' olanlari title a gore goster
    
    # Post.objects.values_list("id", "title","slug") ->postun id leri,postun,title lari,postun slug lari ni goster
    # <QuerySet [(1, '', ''), (2, 'Tiyatro', 'Tiyatro'), (3, 'Resim', 'Resim'), (4, 'Sinema', 'Sinema')]>
    # Post.objects.filter(pk=2).update(title='Telefon')->postun id si 2 olani getir title ni Telefon olarak degistir
    # Post.objects.all().delete()->postun icindeki herseyi silindi


