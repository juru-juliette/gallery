from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.
class LocationTestClass(TestCase):
    '''
    test for Location class
    '''
    # Set up method
    def setUp(self):
        self.loca= Location(country = 'Rwanda')
    def test_instance(self):
        self.assertTrue(isinstance(self.loca,Location))
    def test_save_method(self):
        self.loca.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    def test_update(self):
        self.loca.save_location()
        location= Location.objects.filter(country="Rwanda").first()
        update = Location.objects.filter(id=location.id).update(country="Nigeria")
        updated = Location.objects.filter(country="Nigeria").first()
        self.assertTrue(Location.country,updated.country)


class CategoryTestClass(TestCase):
    '''
    test for category class
    '''
    # Set up method
    def setUp(self):
        self.cat = Category(category='Animmals')
    def test_instance(self):
        self.assertTrue(isinstance(self.cat,Category))
    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)
    def test_update(self):
        self.cat.save_category()
        category= Category.objects.filter(category='Animmals').first()
        update = Category.objects.filter(id=category.id).update(category='Travel')
        updated = Category.objects.filter(category='Travel').first()
        self.assertTrue(Category.category,updated.category)
class ImageTestClass(TestCase):
    '''
    test for Image class
    '''

    def setUp(self):
        self.loca= Location(country= 'Rwanda')
        self.loca.save()
        self.cat = Category(category = 'Animals')
        self.cat.save()
        self.new_image= Image(image = 'dog.jpg',name = 'twin dog',description = 'amazing dogs you can buy',location = self.loca,category = self.cat)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
    def test_save_image(self):
        self.new_image.save()
        new_image = Image.objects.all()
        self.assertTrue(len(new_image) > 0)
    def test_search_image(self):
        images = Image.search_by_category('imag')
        self.assertFalse(len(images)>0)
    def test_get_all_images(self):
        images = Image.objects.all()
        self.assertTrue(Image.name)
    # testing update method
    # def test_update(self):
    #     self.new_image.save_image()
    #     image= Image.objects.filter(name=new_image).first()
    #     update = Image.objects.filter(id=image.id).update(name="juru")
    #     updated = Image.objects.filter(name = "juru").first()
    #     self.assertTrue(Image.name,updated.name)
