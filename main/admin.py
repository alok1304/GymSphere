from django.contrib import admin
from . import models

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display=('text','image_tag')
admin.site.register(models.Banners,BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Service,ServiceAdmin)

class faqAdmin(admin.ModelAdmin):
    list_display=('question','answer')
admin.site.register(models.faq,faqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('full_name','email','location','details','send_time')
admin.site.register(models.Enquiry,EnquiryAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Gallery,GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('text','image_tag')
admin.site.register(models.GalleryImage,GalleryImageAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display=('title','price')
admin.site.register(models.Plan,PlanAdmin)

class PlanFeatureAdmin(admin.ModelAdmin):
    list_display=('feature','plan')
admin.site.register(models.PlanFeature,PlanFeatureAdmin)

