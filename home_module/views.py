from django.shortcuts import render

# Create your views here.

def home_module(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def gallery(request):
    return render(request, 'gallery.html')


def site_header_partial(request):

    return render(request, 'shared/site_header_partial.html')


def site_footer_partial(request):
    return render(request, 'shared/site_footer_partial.html')
