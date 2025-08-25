from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_module, name='index_page_urls'),
    path('contact-us/', views.contact_us, name='contact_us_page'),
    path('gallery/', views.gallery, name='gallery_page'),

]