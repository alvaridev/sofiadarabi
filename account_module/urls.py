from django.urls import path

from account_module.views import LoginPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login_page'),
]
