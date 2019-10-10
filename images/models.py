from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    def save_image(self):
        self.save()

