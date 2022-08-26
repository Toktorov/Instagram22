from django.shortcuts import render, redirect
from posts.models import Post, PostComment, PostLike
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(description__icontains=search_post))
    # else:
    #     # If not searched, return default posts
    #     posts = Post.objects.all().order_by("-title")
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        if 'comment' in request.POST:
            post = Post.objects.get(id = id)
            text = request.POST.get('text')
            comment = PostComment.objects.create(user = request.user, post = post, text = text)
            return redirect('post_detail', post.id)
        if 'like' in request.POST:
            try:
                like = PostLike.objects.get(user=request.user, post = post)
                like.delete()
            except:
                PostLike.objects.create(user = request.user, post = post)
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

def post_update(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        post = Post.objects.get(id = id)
        post.title = title
        post.description = description
        post.image = image 
        post.save()
        return redirect('post_detail', post.id)
    context = {
        'post' : post,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, id):
    post = Post.objects.get(id = id)
    if request.method == "POST":
        post = Post.objects.get(id = id)
        post.delete()
        return redirect('index')
    context = {
        'post' : post,
    }
    return render(request, 'post_delete.html', context)