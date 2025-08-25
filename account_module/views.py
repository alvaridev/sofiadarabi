from django.shortcuts import render
from django.views import View


# Create your views here.


class LoginPageView(View):
    def get(self, request):
        return render(request, 'account_module/login.html')