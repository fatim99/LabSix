from django.shortcuts import render
from .models import blog
# Create your views here.
def Blog(request):
    post=blog.objects.all()
    return render(request,'Blog/Blog.html',{'post':post})

