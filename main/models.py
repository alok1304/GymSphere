from django.db import models
from django.utils.html import mark_safe

# banners
class Banners(models.Model):
    img= models.ImageField(upload_to='banners/')
    text= models.CharField(max_length=150)

    def __str__(self):
        return self.text
    
    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" style="width:50px;" />')
        return "No Image Available"

# service
class Service(models.Model):
    title= models.CharField(max_length=100)
    details= models.TextField()
    img= models.ImageField(upload_to='services/',null=True)

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" style="width:50px;" />')
        return "No Image Available"
    
class faq(models.Model):
    question = models.CharField(max_length=500) 
    answer = models.TextField() 

    def __str__(self):
        return self.question
    

class Enquiry(models.Model):
    full_name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    details= models.TextField()
    send_time= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

# Gallery Model    
class Gallery(models.Model):
    img=models.ImageField(upload_to='Gallery/',null=True)
    title=models.CharField(max_length=100)
    detail=models.TextField()

    def __str__(self):
        return self.title
    
    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" style="width:50px;" />')
        return "No Image Available"


class GalleryImage(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE,null=True)
    img=models.ImageField(upload_to='gallery_img/',null=True)
    text=models.CharField(max_length=100)

    def __str__(self):
        return self.text
    
    def image_tag(self):
        if self.img:
            return mark_safe(f'<img src="{self.img.url}" style="width:50px;" />')
        return "No Image Available"
    

class Plan(models.Model):
    title= models.CharField(max_length=100)
    price= models.CharField(max_length=100)

    def __str__(self):
        return self.title

class PlanFeature(models.Model):
    plan= models.ForeignKey(Plan,on_delete=models.CASCADE)
    feature= models.CharField(max_length=100)

    def __str__(self):
        return self.feature       
