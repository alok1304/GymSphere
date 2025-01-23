from django.shortcuts import render
from . import models,forms
from .forms import UserRegistrationForm
from django.contrib.auth import login
from django.shortcuts import redirect
import stripe
from dotenv import load_dotenv
import os

# Home Page
def home(request):
    banners=models.Banners.objects.all()
    services=models.Service.objects.all()[:3]
    return render(request,'home.html',{'banners': banners,'services':services})

# Enquiry Page
def enquiry(request):
    msg=''
    if request.method=='POST':
        form=forms.EnquiryForm(request.POST)
        if(form.is_valid):
            form.save()
            msg="Message has been Saved."
    form=forms.EnquiryForm
    return render(request,'enquiry.html',{'form': form,'msg': msg})

# faq Page
def faq(request):
    faqs=models.faq.objects.all()
    return render(request,'faq.html',{'faqs': faqs})

# gallery Page
def gallery(request):
    gallery = models.Gallery.objects.all().order_by('-id')
    return render(request,'gallery.html',{'gallerys':gallery})

def pricing(request):
    # Fetch all plans with their related features using prefetch_related for efficiency
    plans = models.Plan.objects.prefetch_related('planfeature_set')
    return render(request, 'pricing.html', {'plans': plans})

# privacy Page
def privacy(request):
    return render(request,'privacy.html')

# terms Page
def terms(request):
    return render(request,'terms.html')


def register(request):
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form =UserRegistrationForm()   
    return render(request,'registration/register.html',{'form':form})


# terms Page
def checkout(request,plan_id):
    planDetail=models.Plan.objects.get(pk=plan_id)
    return render(request,'checkout.html',{'plans':planDetail})


load_dotenv() 
stripe.api_key = os.getenv("STRIPE_API_KEY")

def checkout_session(request,plan_id):
  planDetail=models.Plan.objects.get(pk=plan_id)
  session = stripe.checkout.Session.create(
    payment_method_types=['card'],  
    line_items=[{
      'price_data': {
        'currency': 'inr',
        'product_data': {
          'name': planDetail.title,
        },
        'unit_amount': int(planDetail.price * 100),
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/success',
    cancel_url='http://127.0.0.1:8000/cancel',
  )

  return redirect(session.url, code=303)


# success Page
def success(request):
    return render(request,'success.html')


# cancel Page
def cancel(request):
    return render(request,'cancel.html')