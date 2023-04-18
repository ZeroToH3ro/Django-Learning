from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse("Hello world")


class LoginClass(View):
    def get(self, request):
        return render(request, template_name='Login/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        my_user = authenticate(username=user_name, password=user_pass)

        if my_user is None:
            return HttpResponse('User is not available')

        login(request, my_user)
        return render(request, 'Login/success.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        return HttpResponse('This is view for user')
        
    def post(self, request):
        pass


@decorators.login_required(login_url='/login/')
def view_product(request):
    return HttpResponse("Watch Product")