from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
# Every book has title, description,image, borrowing price, user reviews
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,null=True,blank=True,unique=True)
    def __str__(self):
        return self.name
class BookModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000000)
    image=models.ImageField(upload_to='image/uploads')
    price=models.DecimalField(max_digits=12,decimal_places=2)
    category=models.ManyToManyField(Category,null=True,blank=True)
    def __str__(self):
        return self.title
class Review(models.Model):
    book=models.ForeignKey(BookModel,related_name='review',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    body=models.CharField(max_length=100000)
    RATING_CHOICES=[
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    ]
    rating=models.CharField(max_length=1,choices=RATING_CHOICES)
    def __str__(self):
        return self.body
    
class Borrow(models.Model):
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE,related_name='Borrow')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Borrow')
    borrow_date=models.DateTimeField(auto_now_add=datetime.now())
    return_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.borrow_date)
    
    class Meta:
     ordering = ['borrow_date']




