from djangorocks.blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404


# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })
