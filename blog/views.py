from django.shortcuts import render

# Create your views here.
# Contains the logic of the application
# It will request information from the model and pass it to a template.

def post_list(request):
    return render(request,'blog/post_list.html',{})
