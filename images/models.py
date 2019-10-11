from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    country=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    def __str__(self):
        return self.country
    def save_location(self):
        self.save()
class Category(models.Model):
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category,db_column='category')
    pub_date = models.DateTimeField(auto_now_add=True)
    def save_image(self):
        self.save()
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images
    @classmethod
    def search_by_category(cls,search_term):
        # category = Category.objects.filter(category__icontains=search_term).first()
        image = cls.objects.filter(category__category__contains=search_term)
        return image
    
