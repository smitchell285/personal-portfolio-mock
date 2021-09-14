from django.shortcuts import render
from .models import Blog
from django.views.generic import DetailView
# Create your views here.
def Blogs(request):
    blogs = Blog.objects.all()
    #blogs = Blog.objects.order_by('-date')[:3]
    return render(request,'blog/all_blogs.html',{'blogs':blogs})

class BlogDetail(DetailView):
    model = Blog
