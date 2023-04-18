from django.http import HttpResponse
from django.shortcuts import render
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

# def index(request):
#     return HttpResponse("Hello world")

class IndexClass(View):
    def get(self, request):
        result = '123456'
        return HttpResponse(result)

# def add_post(request):
#     a = PostForm()
#     return render(request, 'news/add_news.html', {"form": a})

class PostClass(View):
    def get(self, request):
        data = PostForm()
        return render(request, 'news/add_news.html', {"form": data})

# def save_news(request):
#     if request.method == "POST":
#         data = PostForm(request.POST)
#         if data.is_valid:
#             data.save()
#             return HttpResponse("Save data")
#         else:
#             return HttpResponse("Data is invalid")
#     else:
#         return HttpResponse("This is not post request")

class SaveNews(View):
    def get(self, request):
        data = PostForm() 
        return render(request, 'news/add_news.html', {'form': data})

    def post(self, request):
        data = PostForm(request.POST)
        if data.is_valid:
            data.save()
            return HttpResponse("Save data")
        else:
            return HttpResponse("Data is invalid")
    
def email_view(request):
    email = SendEmail()
    return render(request, 'news/form_email.html', {"form": email}) 


def process(request):
    if request.method == "POST":
        data = SendEmail(request.POST)
        if data.is_valid():
            title = data.cleaned_data["title"]
            content = data.cleaned_data["content"]
            email = data.cleaned_data["email"]
            cc_email = data.cleaned_data["cc_email"]

            context =  {'title':title, 'content':content, 'cc_email':cc_email, 'email':email}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse("Invalid data")
    else:
            return HttpResponse("This is not post request")