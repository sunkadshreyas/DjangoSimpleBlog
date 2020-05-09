from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
# Contains the logic of the application
# It will request information from the model and pass it to a template.
# Take a post from Models and pass it to template(HTML)

def post_list(request):
    # Published blog posts sorted by published date
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
