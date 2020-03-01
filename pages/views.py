from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings

# Create your views here.
from django.urls import reverse

from blogs.models import Blog
from pages.forms import ContactForm


def home(request):
    blogs = Blog.objects.all().filter(is_home=True).order_by('-pk')[:4]
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            subject = 'Inquiry at ijas.live'
            if data.get('article_ready') == 'yes':
                body_client = "Thank you for your interest. Kindly send your article to ijasliveblogs@gmail.com. " \
                              "We'll alert you once we publish your article."
            else:
                body_client = "Thank you for the message. Our team will get back to you soon, if needed."
            body_admin = f"There is a message from ijas.live. Please go through the details: " \
                         f"\nName: {data.get('name')}\nEmail: {data.get('email')}\n" \
                         f"Message: {data.get('message')}\nInterested to publish article: {data.get('article_ready')}"
            email_from = settings.EMAIL_HOST_USER
            message_client = (subject, body_client, email_from, [form.cleaned_data.get('email')])
            message_admin = (subject, body_admin, email_from, [settings.EMAIL_HOST_USER])
            send_mass_mail((message_client, message_admin), fail_silently=False)
            messages.success(request, "Thank you. Your message has been sent successfully.")
            url = reverse('home')+"#contact"
            return HttpResponseRedirect(url)
    return render(request, 'pages/pages_home.html', {'blogs': blogs, 'form': form})


def about(request):
    return render(request, 'pages/about.html')
