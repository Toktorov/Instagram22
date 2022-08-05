from django.shortcuts import render, redirect
from posts.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    context = {
        'post' : post,
    }
    return render(request, 'post_detail.html', context)

def post_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Post.objects.create(user = request.user, title = title, description = description, image = image)
        return redirect('index')
    return render(request, 'post_create.html')